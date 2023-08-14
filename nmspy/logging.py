from multiprocessing.connection import Connection
import subprocess

import psutil


class stdoutSocket():
    def __init__(self, connection: Connection):
        self.connection = connection

    def write(self, val):
        self.connection.send_bytes(val.encode())

    def flush(self):
        pass


def open_log_console(log_script: str) -> int:
    """ Open the logging console and return the pid of it."""
    cmd = ["cmd.exe", "/c", "start", "NMS.py console", "python", log_script]
    with subprocess.Popen(cmd) as proc:
        log_ppid = proc.pid
    for proc in psutil.process_iter(["pid", "name", "ppid"]):
        if proc.info["ppid"] == log_ppid:
            return proc.info["pid"]
