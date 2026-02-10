import ctypes
import logging

from pymhf import Mod
from pymhf.core._types import CustomTriggerProtocol, DetourTime
from pymhf.core.hooking import hook_manager
from pymhf.gui import no_gui

import nmspy.data.basic_types as basic
import nmspy.data.types as nms
from nmspy.decorators import terminal_command
from nmspy.terminal_parser import TerminalCommand, generate_full_description, split_key

logger = logging.getLogger("chat_bot")


MOD_OPTION = (
    "\n<TITLE>'/mod <><TITLE_BRIGHT>name option(s)<><TITLE>': configure a mod. Enter /mod <><TITLE_BRIGHT>"
    "name<><TITLE> to see options for each mod<>"
)
MOD_LIST_OPTION = "\n<TITLE>'/modlist: display list of mods which can be configured via the terminal<>"


@no_gui
class textChatManager(Mod):
    @terminal_command("Say some words.", "example")
    def say(self, *words):
        logger.info(f"I am saying the words: {' '.join(words)}")

    @nms.cGcTextChatInput.ParseTextForCommands.before
    def intercept_chat_message(
        self,
        this: ctypes._Pointer[nms.cGcTextChatManager],
        lMessageText: ctypes._Pointer[basic.cTkFixedString[0x3FF]],
    ):
        """Parse the command and do something with it.
        We will check for the message starting with `/mod` and recognise this as a command.
        Use the custom callback system in pyMHF to send these commands to anything registered and detect if
        nothing is registered for a given command and raise a helpful message.
        """
        if not lMessageText:
            return
        msg = str(lMessageText.contents)
        if msg.startswith("/pymodlist"):
            # List the available mods which have commands.
            # Filter the keys then generate a set
            mod_command_keys = list(
                filter(lambda x: x.startswith("tc::"), hook_manager.custom_callbacks.keys())
            )
            mod_names = list(set(split_key(x)[0] for x in mod_command_keys))
            mod_names.sort()
            desc = "<TITLE>Available mods with commands<>"
            for mod_name in mod_names:
                desc += f"\n- <TITLE>{mod_name}<>"
            lMessageText.contents.set(desc)
        elif msg.startswith("/mod"):
            # Get the mod name.
            split_msg = msg.split(" ")[1:]
            if len(split_msg) == 0:
                # Invalid...
                lMessageText.contents.set("Need to specify a mod!")
                return
            else:
                if len(split_msg) == 1:
                    # This is just the mod name. Show the help.
                    mod_name = split_msg[0]
                    mod_command_keys = list(
                        filter(
                            lambda x: x.startswith(f"tc::{mod_name}"),
                            hook_manager.custom_callbacks.keys(),
                        )
                    )
                    if not mod_command_keys:
                        lMessageText.contents.set(
                            f"The mod {mod_name!r} either doesn't exist or has no "
                            "terminal commands registered"
                        )
                    else:
                        command_funcs: dict[str, CustomTriggerProtocol] = {}
                        for key in mod_command_keys:
                            funcs = hook_manager.custom_callbacks[key].get(DetourTime.NONE, [])
                            if len(funcs) > 1:
                                logger.warning(
                                    f"Multiple terminal commands have been defined with the key {key}"
                                )
                                return
                            elif len(funcs) == 1:
                                command_funcs[key] = list(funcs)[0]
                        mod_desc = f"<TITLE>{mod_name!r} mod options:<>"
                        for key, func in command_funcs.items():
                            _, command = split_key(key)
                            mod_desc += "\n" + generate_full_description(command, func._description)
                        lMessageText.contents.set(mod_desc)
                        return
                elif len(split_msg) == 2:
                    parsed_command = TerminalCommand(split_msg[0], split_msg[1], [])
                elif len(split_msg) > 2:
                    parsed_command = TerminalCommand(split_msg[0], split_msg[1], split_msg[2:])
                try:
                    # Call the custom callback with the generated key.
                    # If it doesn't exist we raise an exception which we catch and then show a message in the
                    # terminal.
                    hook_manager.call_custom_callbacks(
                        parsed_command.callback_key,
                        args=parsed_command.args,
                        alert_nonexist=True,
                    )
                    lMessageText.contents.set(
                        f"Ran command {parsed_command.command_name!r} for mod {parsed_command.mod_name!r}"
                    )
                except ValueError:
                    lMessageText.contents.set(
                        f"Invalid command {parsed_command.command_name!r} for mod {parsed_command.mod_name!r}"
                    )
                    # Let's get the list of actual commands for this mod.
                    mod_command_keys = list(
                        filter(
                            lambda x: x.startswith(f"tc::{parsed_command.mod_name}"),
                            hook_manager.custom_callbacks.keys(),
                        )
                    )
                    if not mod_command_keys:
                        lMessageText.contents.set(
                            f"The mod {parsed_command.mod_name!r} either doesn't exist or has no "
                            "terminal commands registered"
                        )
                    else:
                        command_funcs: dict[str, CustomTriggerProtocol] = {}
                        for key in mod_command_keys:
                            funcs = hook_manager.custom_callbacks[key].get(DetourTime.NONE, [])
                            if len(funcs) > 1:
                                logger.warning(
                                    f"Multiple terminal commands have been defined with the key {key}"
                                )
                                return
                            elif len(funcs) == 1:
                                command_funcs[key] = list(funcs)[0]
                        mod_desc = f"<TITLE>{parsed_command.mod_name!r} mod options:<>"
                        for key, func in command_funcs.items():
                            _, command = split_key(key)
                            mod_desc += "\n" + generate_full_description(command, func._description)
                        lMessageText.contents.set(mod_desc)

    @nms.cGcTextChatManager.Say.before
    def say_chat_message(
        self,
        this: ctypes._Pointer[nms.cGcTextChatManager],
        lsMessageBody: ctypes._Pointer[basic.cTkFixedString[0x3FF]],
        lbSystemMessage: bool,
    ):
        if lsMessageBody:
            msg = str(lsMessageBody.contents)
            # Check for the message which the game generates for an invalid command and add the mod command.
            if msg.startswith("<TITLE>") and msg.split("\n")[0].endswith("commands:"):
                msg = msg + MOD_OPTION + MOD_LIST_OPTION
                lsMessageBody.contents.set(msg)
