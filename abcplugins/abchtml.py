from typing import Coroutine
from bs4 import BeautifulSoup
from aiohttp.web import Application, get, Response
from abcbase import ABCError, ABClass
from abcbinder import ABCBinder, ABCPhoto

class ABCParsError(ABCError): pass

class ABCHTMLParcer(ABClass):
	def __init__(self, app:Application=None):
		self.application = app
		# 'gif': 	  	'image/gif'
		# 'jpeg': 	  	'image/jpeg'
		# 'png': 	  	'image/png'
		# 'tiff': 	  	'image/tiff'
		# 'x-icon':   	'image/x-icon'
		# 'vnd.djvu': 	'image/vnd.djvu'
		# 'svg+xml':  	'image/svg+xml'
		# 'css': 	  	'text/css'
		# 'csv': 	  	'text/csv'
		# 'html': 	  	'text/html'
		# 'javascript': 'text/javascript'
		# 'plain': 		'text/plain'
		# 'xml': 		'text/xml'
		# 'MPEG': 		'video/mpeg'
		# 'MP4': 		'video/mp4'
		# 'OGG': 		'video/ogg'
		# 'WebM': 		'video/webm'
		# 'WMV': 		'video/x-ms-wmv'
		# 'FLV': 		'video/x-flv'
		# 'AVI': 		'video/x-msvideo'

	def set_server_paths(self, path_to_html_file:str) -> Application:
		with open(path_to_html_file, 'r', encoding='utf-8') as html:
			lines = html.read()
		html = BeautifulSoup(lines)
		src_script = list(map(lambda x: x['src'], html.find_all('script')))
		src_img = list(map(lambda x: x['src'], html.find_all('img')))
		self.app.add_routes(
			[
				get(
					[
						link_obj['href'],
						self._get_coro(link_obj['href'])
					]
				) 
				for link_obj in (html.find_all('link'))
				if (link_obj['rel'].lower() == 'stylesheet') and (not link_obj['href'].startswith('http'))
			]
		)
		self.app.add_routes(
			[
				get(
					[
						script_obj['src'],
						self._get_script(script_obj['src'])
					]
				)
				for script_obj in src_script
				if not (script_obj['href'].startswith('http'))
			]
		)
		self.app.add_routes(
			[
				get(
					[
						img_obj['src'],
						self._get_script(img_obj['src'])
					]
				)
				for img_obj in src_img
				if not (img_obj['href'].startswith('http'))
			]
		)
		return self.app

	def _get_coro(self, path:str) -> Coroutine:
		async def _css_getter(request) -> Response:
			file_commander = ABCBinder(filename=path)
			lines = await file_commander._get()
			return Response(
				body=lines,
				content_type='text/css'
			)
		return _css_getter

	def _get_script(self, path:str) -> Coroutine:
		async def _js_getter(request) -> Response:
			file_commander = ABCBinder(filename=path)
			lines = await file_commander._get()
			return Response(
				body=lines,
				content_type='text/css'
			)
		return _js_getter

	def _get_bytes(self, path:str, type:str='image/png') -> Coroutine:
		async def _photo_getter(request) -> Response:
			file_commander = ABCPhoto(filename=path)
			byte = await file_commander._get_bytes()
			return Response(
				body=byte,
				content_type='text/css'
			)
		return _photo_getter