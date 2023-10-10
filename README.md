# How to use this ~~shit~~ program
Everything is very easy! Add the project to your directory and immediately start importing.
Here's an example:
<blockquote> There will be examples here in the future </blockquote>

## What's wrong with that?
It's very simple! This directory can make life a little easier for those people who make bots with a web admin panel. For example:
```Python
from aiohttp.web import Application
from abctg import ABCHTMLParcer

abchtml = ABCHTMLParcer(app=Application())
app = abchtml.set_server_paths('/path/to/your/html/file.html')
```
and that's it! You will already have preloaded scripts, styles and photos! If you wish, you can even add something of your own (hints on content_type) are in the file. They are inside the comments, or you can look [here](https://en.wikipedia.org/wiki/MIME#:~:text=Multipurpose%20Internet%20Mail%20Extensions%20(MIME),specified%20in%20non-ASCII%20character%20sets)
But there are other examples of using different classes

json.json
```JSON
{
	"example": {
		"to": 123,
		"you": "Help"
	}
}
```

test.py
```Python
from abctg import ABCJson

json_getter = ABCJson(filename='json.json')
print(await json_getter.get()) # {'example': {'to': 123, 'you': 'help'}}
```

There is also an example of using telegram bot
```Python
import asyncio

from os import getenv
from aiogram import Bot
from aiogram.types import Message
from abctg import ABCTelegram

constructor = ABCTelegram(
	bot=Bot(getenv("token")),
	loop=asyncio.new_event_loop()
)

...

@constructor.dp.message_handler(commands=['qwerty'])
async def qwerty_handler(message:Message):
	...
```
or
```Python
import asyncio

from os import getenv
from aiogram.types import Message
from abctg import ABCTelegram

constructor = ABCTelegram(
	token=getenv("token"),
	loop=asyncio.new_event_loop()
)

...

@constructor.dp.message_handler(commands=['qwerty'])
async def qwerty_handler(message:Message):
	...
```

Example of using abcasync
```Python
import asyncio

from importpath import importclass
from abctg import ABCAsyncStarter

starter = ABCAsyncStarter()

...

if __name__ == '__main__':
	starter.start(
		polling(),
		awaiting(),
		app_starter()
	)
```