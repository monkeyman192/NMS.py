import asyncio
import concurrent.futures
import configparser
from functools import partial
import os
import os.path as op
from signal import SIGTERM
import time


import pymem
import pymem.process

from nmspy.caching import hash_bytes
from nmspy.process import start_process
from nmspy.protocols import ESCAPE_SEQUENCE, TerminalProtocol
from nmspy.logging import open_log_console


CWD = op.dirname(__file__)


# Parse the config file first so we can load anything we need to know.
config = configparser.ConfigParser()
# Currently it's in the same directory as this file...
cfg_file = op.join(CWD, "NMS.py.cfg")
read = config.read(cfg_file)
binary_path = config["NMS"]["path"]
root_dir = config["NMS"]["root_dir"]


# Steam:
# binary_path = "C:/Program Files (x86)/Steam/steamapps/common/No Man's Sky/Binaries/NMS.exe"
# GOG 4.13, aka, "the good shit":
# binary_path = "C:/Games/No Man's Sky/Binaries/NMS.exe"
executor = None
futures = []
loop = asyncio.get_event_loop()


def kill_injected_code(loop):
    # End one last "escape sequence" message:
    client_completed = asyncio.Future()
    client_factory = partial(
        TerminalProtocol,
        message=ESCAPE_SEQUENCE.decode(),
        future=client_completed
    )
    factory_coroutine = loop.create_connection(
        client_factory,
        '127.0.0.1',
        6770,
    )
    loop.run_until_complete(factory_coroutine)
    loop.run_until_complete(client_completed)


try:
    log_pid = open_log_console(op.join(CWD, "log_terminal.py"))
    # Have a small nap just to give it some time.
    time.sleep(0.5)
    print(f"Opened the console log with PID: {log_pid}")
    with open(binary_path, "rb") as f:
        binary_hash = hash_bytes(f)
    print(f"Exe hash is: {binary_hash}")

    process_handle, thread_handle, pid, tid = start_process(binary_path, creationflags=0x4)
    print(f'Opened NMS with PID: {pid}')
    # Wait some time for the data to be written to memory.
    time.sleep(3)

    # Get the base address
    nms = pymem.Pymem('NMS.exe')
    print(f"proc id from pymem: {nms.process_id}")
    nms.inject_python_interpreter()
    pb = nms.process_base
    binary_base = pb.lpBaseOfDll
    binary_size = pb.SizeOfImage
    # Inject the base address as a "global" variable into the python interpreter
    # of NMS.exe
    print(f"The NMS handle: {nms.process_handle}, base: 0x{binary_base:X}")

    # Inject some other dlls:
    # pymem.process.inject_dll(nms.process_handle, b"path")

    cwd = CWD.replace("\\", "\\\\")
    nms.inject_python_shellcode(f"CWD = '{cwd}'")
    nms.inject_python_shellcode("import sys")
    nms.inject_python_shellcode("sys.path.append(CWD)")

    # Inject _preinject AFTER modifying the sys.path for now until we have
    # nmspy installed via pip.
    with open(op.join(CWD, "nmspy", "_scripts", "_preinject.py"), "r") as f:
        _preinject_shellcode = f.read()
    nms.inject_python_shellcode(_preinject_shellcode)
    # Inject the common NMS variables which are required for general use.
    nms.inject_python_shellcode(f"nmspy._internal.BASE_ADDRESS = {binary_base}")
    nms.inject_python_shellcode(f"nmspy._internal.SIZE_OF_IMAGE = {binary_size}")
    nms.inject_python_shellcode(f"nmspy._internal.CWD = '{cwd}'")
    nms.inject_python_shellcode(f"nmspy._internal.HANDLE = {nms.process_handle}")
    nms.inject_python_shellcode(f"nmspy._internal.BINARY_HASH = '{binary_hash}'")
    nms.inject_python_shellcode(
        f"nmspy._internal.NMS_ROOT_DIR = \"{root_dir}\""
    )
    # Inject the script
    with open(op.join(CWD, "injected.py"), "r") as f:
        shellcode = f.read()
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
    print("Injecting hooking code")
    futures.append(executor.submit(nms.inject_python_shellcode, shellcode))

    try:
        input("Press something to start NMS")
    except KeyboardInterrupt:
        # Kill the injected code so that we don't wait forever for the future to end.
        kill_injected_code(loop)
        raise
    print(f"Opening thread {thread_handle}")
    # thread_handle = pymem.process.open_thread(main_thread.thread_id)
    pymem.ressources.kernel32.ResumeThread(thread_handle)

    print("NMS.py interactive python command prompt")
    print("Type any valid python commands to execute them within the NMS process")
    while True:
        try:
            input_ = input(">>> ")
            client_completed = asyncio.Future()
            client_factory = partial(
                TerminalProtocol,
                message=input_,
                future=client_completed
            )
            factory_coroutine = loop.create_connection(
                client_factory,
                '127.0.0.1',
                6770,
            )
            loop.run_until_complete(factory_coroutine)
            loop.run_until_complete(client_completed)
        except KeyboardInterrupt:
            kill_injected_code(loop)
            raise
except KeyboardInterrupt:
    # If it's a keyboard interrupt, just pass as it will have bubbled up from
    # below.
    pass
except Exception as e:
    # Any other exception we want to actually know about.
    print(e)
    raise
finally:
    loop.close()
    try:
        for future in concurrent.futures.as_completed(futures, timeout=5):
            print(future)
    except TimeoutError:
        # Don't really care.
        print("Got a time out error...")
        pass
    if executor is not None:
        executor.shutdown(wait=False)
    try:
        with open(op.join(CWD, "end.py"), "r") as f:
            close_shellcode = f.read()
        nms.inject_python_shellcode(close_shellcode)
        print("Just injected the close command?")
        # Kill the NMS process.
    except:
        pass
    finally:
        print("Forcibly shutting down NMS")
        time.sleep(1)
        for _pid in {nms.process_id, pid, log_pid}:
            try:
                os.kill(_pid, SIGTERM)
                print(f"Just killed process {_pid}")
            except:
                # If we can't kill it, it's probably already dead. Just continue.
                print(f"Failed to kill process {_pid}. It was likely already dead...")
                pass
