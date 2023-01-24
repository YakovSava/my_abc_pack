import asyncio

from json import load
from aiohttp import ClientSession
from fake_useragent import UserAgent
from .abcbase import ABClass, ABCError

class ABCConnectorError(ABCError): pass

class ABCConnector(ABClass):
	def __init__(self,
		loop:asyncio.AbstractEventLoop=asyncio.get_event_loop(),
		custom_connector:ClientSession=None,
		proxy:str=None
	):
		self.loop = loop
		self.session = custom_connector if custom_connector is not None else loop.run_until_complete(self._construct())
		self.agent = UserAgent()
		self.parameters = {
			'proxy': proxy,
			'headers': {"user-agent": self.agent.random}
		}

	async def change_user_agent(self):
		self.parameters['headers'] = {"user-agent": self.agent.random}

	async def _construct(self):
		self.session = ClientSession(trust_env=True)
		return self.session

	async def _get_raw(self, url:str) -> str:
		async with self.session.get(url, **self.parameters) as resp:
			if resp.status == 200:
				lines = await resp.read()
			else:
				raise ABCConnectorError
		return lines.decode()

	async def _get_json(self, url:str) -> dict:
		lines = await self._get_raw(url)
		return load(lines)