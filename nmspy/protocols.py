import asyncio
import builtins
import traceback

from functools import partial

# This escape sequence is arbitrarily the first 4 digits of Euler's number "e"
# written as bytes from left to right.
ESCAPE_SEQUENCE = b"\x02\x07\x01\x08"


class ExecutionEndedException(Exception):
    pass


def custom_exception_handler(loop: asyncio.AbstractEventLoop, context: dict):
    # Simple custom exception handler to stop the loop if an
    # ExecutionEndedException exception is raised.
    exception = context.get("exception")
    if isinstance(exception, ExecutionEndedException):
        loop.stop()


class TerminalProtocol(asyncio.Protocol):
    def __init__(self, message: str, future):
        super().__init__()
        self.message = message
        self.future = future

    def connection_made(self, transport):
        self.transport = transport
        transport.write(self.message.encode())
        if transport.can_write_eof():
            transport.write_eof()

    def data_received(self, data):
        print(data.decode(), end="")

    def eof_received(self):
        self.transport.close()
        if not self.future.done():
            self.future.set_result(True)

    def connection_lost(self, exc):
        self.transport.close()
        if not self.future.done():
            self.future.set_result(True)
        super().connection_lost(exc)
