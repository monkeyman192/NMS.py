# NMS.py

NMS.py is a python library to expose interal game functions for No Man's Sky.

**NOTE:** This library is missing a lot of info which will gradually get added over time.
It should also be noted that Game updates can very easily break mods utilising NMS.py, so care should be taken when using mods.
Any responsibility for broken saves is entirely on the users of this library.

Also note that this library will never contain functions relating to online functionality to avoid any abuse.
The author of this library condones any use of this for any usage that is detrimental to other players.

## Installation

**Note:** Before you start: NMS.py can only run on python 3.9 - 3.11 inclusive. Newer versions are not supported due to issues injecting python into them unfortunately.
It is recommended that you download python from the [official site](https://www.python.org/downloads) as the windows store version may have issues, as well as the managed python which [uv](https://docs.astral.sh/uv/) installs.

The recommended way to install NMS.py is to simply run `python -m pip install nmspy`. This will install NMS.py and its' dependency [`pyMHF`](https://github.com/monkeyman192/pyMHF) into your system python. You can of course install it in a venv or as a dependency using uv if you prefer.

## Usage

To run NMS.py, enter the following command into a terminal:
```
pymhf run nmspy
```

This will display some config options to complete. The only option to consider is the location of the mods folder. It is recommended that you create a new folder inside the normal MODS folder which can contain all the python scripts you want to be run.

If NMS.py starts up successfully you should see two extra windows; an auto-created GUI from pyMHF, and a terminal window which will show the logs for pyMHF.

If you want to stop NMS, you can press `ctrl + C` in the window you started the process in to kill it.

### Credits

Thanks to the developers of minhook, cyminhook and pymem, all of which are instrumental in making this framework possible.

Big thanks to [vitalised](https://github.com/VITALISED) for their constant RE discussions, and [gurren3](https://github.com/gurrenm3) for the same as well as the initial work done on NMS.API which heavily inspired the creation of this.

Thanks also to the many people I have discussed various NMS details with, both big and small.

Thanks to [RaYRoD](https://github.com/RaYRoD-TV) for initially discovering the pdb as well as regular insightful discussions regarding all things reverse engineering NMS.

Thanks also to anyone who has contributed function definitions or patterns. Any and all help is always appreciated!
