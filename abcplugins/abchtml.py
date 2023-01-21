from bs4 import BeautifulSoup
from aiofiles import open as aiopen
from aiohttp.web import Application
from abcbase import ABCError, ABClass

class ABCParsError(ABCError): pass

class ABCHTMLParcer(ABClass):
	def __init__(self, app:Application=None):
		self.application = app
		self.all_types = {
			'image': {
				'gif': 'image/gif',
				'jpeg': 'image/jpeg',
				'png': 'image/png',
				'tiff': 'image/tiff',
				'x-icon': 'image/x-icon',
				'vnd.djvu': 'image/vnd.djvu',
				'svg+xml': 'image/svg+xml'
			},
			'text': {
				'css': 'text/css',
				'csv': 'text/csv',
				'html': 'text/html',
				'javascript': 'text/javascript',
				'plain': 'text/plain',
				'xml': 'text/xml'
			},
			'video': {
				'MPEG': 'video/mpeg',
				'MP4': 'video/mp4',
				'OGG': 'video/ogg',
				'WebM': 'video/webm',
				'WMV': 'video/x-ms-wmv',
				'FLV': 'video/x-flv',
				'AVI': 'video/x-msvideo'
			}
		}
		self.all_types_list = []
		for one in list(self.all_types.values()):
			self.all_types_list.extend([i for i in list(one.values())])

	def _check(self, rel:str) -> bool: return rel in self.all_types_list

	async def set_server_paths(self, path_to_html_file:str) -> list:
		async with aiopen(path_to_html_file, 'r', encoding='utf-8') as html:
			lines = await html.read()
		html = BeautifulSoup(lines)
		link = html.find_all('link')
		src_script = list(map(lambda x: x['src'], html.find_all('script')))
		src_img = list(map(lambda x: x['src'], html.find_all('img')))
		for link_obj in link:
			if link_obj['rel'].lower() == 'stylesheet':
				