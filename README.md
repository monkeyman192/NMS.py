# NMS.py

NMS.py, a python hooking and modding library for No Man's Sky.

**NOTE:** This is a heavy WIP. The API is NOT considered stable currently and a decent amount of data is missing and/or wrong.

## Usage

1. Ensure that python 3.9+ is installed
1. Install the required dependencies. Run the following in the current directory: `python -m pip install -r requirements.txt`
1. Modify `NMS.py.cfg` to have the correct binary path. Note that currently the only supported binary is the one which has the hash listed in the file. You can check the hash of your NMS binary by running `certutil -hashfile "NMS.exe" SHA1` in the directory with the NMS.exe binary.
1. in a terminal run `python main.py`

You should have another popup appear with the NMS.py logo at the top, and then a series of log messages.
If this doesn't occur then your firewall may be blocking the port 6770, so make sure that a TCP connection is allowed on this port on your local network (ie. 127.0.0.0, or possibly 0.0.0.)

If all goes well you should see `"Serving on executor ('127.0.0.1', 6770)"`
Once you see this message you are fine to press anything in the other window where you entered `python main.py`.

Any exceptions will be logged to a file named `CRITICAL_ERROR.txt`, and logs will be placed in a `logs` directory.

- If you want to stop NMS, you can press `ctrl + C` in the window you started the process in to kill it.


### Credits

Thanks to the developers of minhook, cyminhook and pymem, all of which are instrumental in making this framework possible.

Big thanks to [vitalised](https://github.com/VITALISED) for their constant RE discussions. and [gurren3](https://github.com/gurrenm3) for the same as well as the initial work done on NMS.API which heavily inspired the creation of this.

Thanks also to the many people I have discussed various NMS details with, both big and small.

Thanks to rayrod for initially discovering the pdb.
