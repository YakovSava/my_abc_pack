from os import listdir
from sys import platform
from ctypes import *
from abcbase import ABCError, ABClass


class ABCDllError(ABCError):
    pass


class ABCDllUploader(ABClass):
    def __init__(self, dll_path: str=''):
        self.dlls = {}
        if platform in ['linux', 'linux2']:
            end = '.so'
        elif platform in ['win32', 'cygwin', 'msys']:
            end = '.dll'
        else:
            raise ABCDllError
        for file in listdir(dll_path):
            if file.endswith(end):
                self.dlls[file.split('.')[0]] = CDLL(f'./{dll_path}/{file}')

    async def get(self, name: str) -> CDLL or None:
        return self.dlls.get(name)

    def __index__(self, name: str) -> CDLL or None:
        return self.dlls.get(name)

    def __getattr__(self, name: str) -> CDLL or None:
        return self.dlls.get(name)
