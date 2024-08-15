# NMS.py

NMS.py, a python hooking and modding library for No Man's Sky.

**NOTE:** This is a heavy WIP. The API is NOT considered stable currently and a decent amount of data is missing and/or wrong.

## Installation

There are two ways to install NMS.py.

### Basic installation

This method is for those who don't use python much or are not familiar with the python ecosystem (ie. virtual environments etc).

1. Download a version of python [3.9](https://www.python.org/downloads/release/python-3913/) or [3.10](https://www.python.org/downloads/release/python-31011/) from the official python site.
Note: Later versions of python may work (eg. 3.11), however pymem seems to have issues injecting them sometimes it seems, so I find it better to stick to a slightly older version for simplicity.
1. Clone/download this repository to somewhere on your computer.
1. Open `cmd` in the directory this was downloaded to. This can be done most easily by typing `cmd` in the explorer path bar.
1. Run `python -m pip install .`
  This should install all the dependencies including pulling the latest [`pyMHF`](https://github.com/monkeyman192/pyMHF) from GitHub which is the core framework which is used to power `NMS.py`.

### Advanced installation

This method is more suited for those who want to modify `pyMHF` or `NMS.py` as it doesn't involve installing `NMS.py`, but will just run `NMS.py` in local mode.
This will assume some experience with python.

1. Clone both [`pyMHF`](https://github.com/monkeyman192/pyMHF) and `NMS.py` into separate folders. I recommend creating a directory and then cloning both into that directory so that the folders are siblings.
1. Install `pyMHF` in editable mode. This can done in either a virtual envirnonment or using the system python by running `python -m pip install -e .` in the `pyMHF` folder.
1. In the `NMS.py` folder, edit the `pymhf.cfg` file. Depending on whether or not you are wanting to run the old version of the game (4.13), or the latest on steam, will change what settings to change. (See `settings` section below)
1. In the `pymhf` folder add a python file called `run_nms.py` which looks like the following:
```py
from pymhf import load_module

DIR = "<absolute path to NMS.py/nmspy folder>"

load_module("nmspy", DIR, True)
```
5. Run `python ./run_nms.py`

## Usage

The following is for anyone running `NMS.py` as per the "Basic Installation" above.

1. Run `pymhf nmspy`. The first time this is run it will copy the config file over to your appdata folder (`%AppData%/pymhf/nmspy`) and it will guide you through configuring `NMS.py`.
If you ever want to return to this configuration menu, run `python --config nmspy`.
1. Once the game has been configured, you will have an option to run it. Selecting `y` should run the game. This will create a popup with the `pyMHF` logo and this is your log terminal.
If this doesn't occur then your firewall may be blocking the port 6770, so make sure that a TCP connection is allowed on this port on your local network (ie. 127.0.0.0, or possibly 0.0.0.0)

If all goes well you should see `"Serving on executor ('127.0.0.1', 6770)"`.

If the game starts paused, you'll need to press the return key on your keyboard in the console window that `pymhf nmspy` was run from to start the game properly.

Any exceptions will be logged to a file named `CRITICAL_ERROR.txt`, and logs will be placed in a `logs` directory.

If you want to stop NMS, you can press `ctrl + C` in the window you started the process in to kill it.

## Settings

Depending on what version of NMS you are running, you'll need to change different settings:

### Running NMS 4.13 (Fractals)

`[binary]`:
- `path`: The absolute path to the `NMS.exe` which is to be run.
- `steam_gameid`: This key should be either commented out or not present.
- `mod_dir`: The absolute path to the directory containing mods.
- `start_paused`: Should be `True`. This can be `False`, but you get better hook coverage with the value set to `True`.

### Running latest Steam version

`[binary]`:
- `steam_gameid`: This should have the value `275850`.
- `mod_dir`: The absolute path to the directory containing mods.
- `internal_mod_dir`: This key should be either commented out or not present for now.
- `start_paused`: Must be `False`.


### Credits

Thanks to the developers of minhook, cyminhook and pymem, all of which are instrumental in making this framework possible.

Big thanks to [vitalised](https://github.com/VITALISED) for their constant RE discussions. and [gurren3](https://github.com/gurrenm3) for the same as well as the initial work done on NMS.API which heavily inspired the creation of this.

Thanks also to the many people I have discussed various NMS details with, both big and small.

Thanks to rayrod for initially discovering the pdb.
