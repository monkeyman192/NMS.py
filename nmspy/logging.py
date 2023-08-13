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
    """ Openthe logging console and return the pid of it."""
    with subprocess.Popen(["cmd.exe", "/c", "start", "", "python", log_script]) as proc:
        log_ppid = proc.pid
    for proc in psutil.process_iter(["pid", "name", "ppid"]):
        if proc.info["ppid"] == log_ppid:
            return proc.info["pid"]
