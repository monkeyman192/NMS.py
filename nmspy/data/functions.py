import ctypes

import nmspy.data.enums as enums
from nmspy.calling import call_function
from nmspy.memutils import NMSStruct


class cTkInputPort(NMSStruct):
    _fields_ = [
        ("inputManager", ctypes.c_longlong),
        # TODO: Add more...
    ]

    inputManager: int

    def SetButton(self, leIndex: enums.eInputButton) -> None:
        """ Set the provided button as pressed. """
        return call_function("cTkInputPort::SetButton", self._offset, leIndex)

    @staticmethod
    def SetButton_(this: int, leIndex: enums.eInputButton) -> None:
        """ Set the provided button as pressed for the provided instance. """
        return call_function("cTkInputPort::SetButton", this, leIndex)
