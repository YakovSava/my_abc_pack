from abcbase import *
from abcbinder import *
from abcasync import *
from abchtml import *
from abconnector import *
from abctelegram import *
from abcxx import *

ALL = {
	'base': [
		ABClass,
		ABCError,
		ABCMethod,
		ABCWith,
		ABCAsyncWith,
		ABCIterator,
		ABCAsyncIterator,
		ABCStorage
	],
	'binder': [
		ABCBinderError,
		ABCBinder,
		ABCJson,
		ABCPhoto
	],
	'async': [
		ABCAsyncError,
		ABCAsyncStarter
	],
	'html': [
		ABCParsError,
		ABCHTMLParcer
	],
	'connector': [
		ABCConnectorError,
		ABCConnector
	],
	'telegram': [
		ABCTelegramBotError,
		ABCTelegramDispatcher,
		ABCTelegram
	],
	'cxx': [
		ABCDllError,
		ABCDllUploader
	]
}