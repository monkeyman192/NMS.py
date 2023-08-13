import ctypes
import ctypes.wintypes
import _winapi


class SECURITY_ATTRIBUTES(ctypes.Structure):
    _fields_ = [
        ("nLength", ctypes.wintypes.DWORD),
        ("lpSecurityDescriptor", ctypes.wintypes.LPVOID),
        ("bInheritHandle", ctypes.wintypes.BOOL),
    ]


def start_process(binary_path: str, creationflags: int = 0x0):
    # Start an executable similarly to subprocess.Popen
    # The functionality here is ripped directly from that implementation,
    # however we don't discard the thread_handle here so that we may use it
    # again later to resume the thread if we pause it.
    proc_attr = SECURITY_ATTRIBUTES()
    proc_attr.bInheritHandle = True
    thread_attr = SECURITY_ATTRIBUTES()
    thread_attr.bInheritHandle = True
    # Start the process the internal way to get the thread handle.
    handle_process, handle_thread, pid, tid = _winapi.CreateProcess(
        None,
        binary_path,
        ctypes.byref(proc_attr),
        ctypes.byref(thread_attr),
        0,
        creationflags,
        None,
        None,
        None,
    )
    return (handle_process, handle_thread, pid, tid)
