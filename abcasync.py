import asyncio

from typing import Coroutine
from .abcbase import ABClass, ABCError


class ABCAsyncError(ABCError):
    pass


class ABCAsyncStarter(ABClass):
    def __init__(self, loop: asyncio.AbstractEventLoop=None):
        self.loop = loop if loop is not None else asyncio.get_event_loop()

    def _start(self, *futures: Coroutine):
        return self.loop.run_until_complete(
            asyncio.wait([
                self.loop.create_task(coro)
                for coro in futures
            ])
        )
