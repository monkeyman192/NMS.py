class UnknownFunctionError(Exception):
    pass


class HookError(Exception):
    def __init__(self, status, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.status = status


class NoSaveError(Exception):
    pass
