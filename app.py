!pip install adafruit-io --quiet
!pip install python-telegram-bot==13.0 --quiet
from Adafruit_IO import Client
aio = Client('HEMACHANDRAN_V','aio_btZi81nDifoh9B6kKTtir77ZgpQu')
from telegram.ext import Updater, MessageHandler, Filters

def demo1(bot,update):
  aio.send('light',1)
  chat_id = bot.message.chat_id
  bot.message.reply_text('Light turned on')

def demo2(bot,update):
  aio.send('light',0)
  chat_id = bot.message.chat_id
  bot.message.reply_text('Light turned off') 

def demo3(bot,update):
  aio.send('fan',1)
  chat_id = bot.message.chat_id
  bot.message.reply_text('Fan turned on')

def demo4(bot,update):
  aio.send('fan',0)
  chat_id = bot.message.chat_id
  bot.message.reply_text('Fan turned off')

def main(bot,update):
  a= bot.message.text
  if a =="Turn on light":
    demo1(bot,update)
  elif a =="Turn off light":
    demo2(bot,update)
  elif a =="Turn on fan":
    demo3(bot,update)
  elif a =="Turn off fan":
    demo4(bot,update)

bot_token = '1982159235:AAH7rqKN9Uw-kQ9yE_cFSxnZsDga05cs9Pk'
u = Updater(bot_token,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()
