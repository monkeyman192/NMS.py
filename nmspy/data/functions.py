import nmspy.data.enums as enums
from nmspy.calling import call_function


class cTkInputPort:
    @staticmethod
    def SetButton(this: int, leIndex: enums.eInputButton) -> None:
        return call_function("cTkInputPort::SetButton", this, leIndex)
