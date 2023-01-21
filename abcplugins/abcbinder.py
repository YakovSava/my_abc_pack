from os.path import join, exists
from typing import Any
from aiofiles import open as aiopen
from abcbase import ABClass, ABCError

class ABCBinderError(ABCError): pass

class ABCBinder(ABClass):

	def __init__(self, filename:str=None, path:str=None):
		if (not filename) and (not path):
			raise ABCBinderError
		elif (not path):
			self.filename = filename
		else:
			self.filename = join(path, join)

	async def _get(self) -> str:
		async with aiopen(self.filename, 'r', encoding='utf-8') as file: return await file.read()

	async def _set(self, string:Any) -> None:
		async with aiopen(self.filename, 'w',encoding='utf-8') as file: await file.write(f'{string}')

	def __bool__(self):
		return exists(self.filename)
		
class ABCJson(ABCBinder):
	async def get(self) -> dict:
		lines = await self._get()
		return eval(f'{lines}')