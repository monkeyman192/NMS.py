# A collection of useful variables or stateful objects which can be accessed or used by all mods.
# These are often designed to avoid conflicts between mods by allowing NMS.py to generate ID's or such.

import multiprocessing
from ctypes import c_uint32
from multiprocessing.sharedctypes import Synchronized


class UniqueCounter:
    def __init__(self):
        # Create a value which will always start at 0
        self._counter: Synchronized[int] = multiprocessing.Value(c_uint32, 0)

    def get(self) -> int:
        """Get the next unique index value"""
        with self._counter.get_lock():
            value = self._counter.value
            self._counter.value += 1
            return value


unique_counter = UniqueCounter()
