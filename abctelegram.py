from asyncio import AbstractEventLoop
from multiprocessing import Process
from aiogram import Bot, Dispatcher, executor
from abcbase import ABCError, ABClass


class ABCTelegramBotError(ABCError):
    pass


class ABCTelegramDispatcher(ABCError):
    pass


class ABCTelegram(ABClass):
    def __init__(self,
                 dp: Dispatcher=None,
                 bot: Bot=None,
                 custom_executor: executor=None,
                 token: str=None,
                 loop: AbstractEventLoop=None
                 ):
        if (token is None) and (bot is None):
            raise ABCTelegramBotError
        self.bot = bot if bot is not None else Bot(token=token)
        self.dp = bot if dp is not None else Dispatcher(self.bot)
        self.executor = custom_executor if custom_executor is not None else executor
        self.loop = loop

    def polling(self):
        process = Process(target=self.executor.start_polling, args=(
            self.dp,), kwargs={'skip_updates': True, 'loop': self.loop})
        process.start()
