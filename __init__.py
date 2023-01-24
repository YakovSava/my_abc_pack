from abctg.abcbase import *
from abctg.abcbinder import *
from abctg.abcasync import *
from abctg.abchtml import *
from abctg.abconnector import *
from abctg.abctelegram import *
from abctg.abcxx import *

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