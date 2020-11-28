from Adafruit_IO import Client, Feed , Data
import os
ADAFRUIT_IO_USERNAME = os.getenv('ADAFRUIT_IO_USERNAME')
ADAFRUIT_IO_KEY = os.getenv('ADAFRUIT_IO_KEY')
TOKEN = os.getenv('TOKEN')
aio = Client(ADAFRUIT_IO_USERNAME,ADAFRUIT_IO_KEY)

def send_value(value):
    feed = aio.feeds('tgbot')
    aio.send_data(feed.key,value)

from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
import requests
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(update, bot):
  update.message.reply_text("/Turnon : To turn on the light /Turnoff : To turn off the light")

def Turnon(update, bot):
  update.message.reply_text("Light turned on,value=1 sent to adafruit_io feed")
  bot.send_photo( chat_id = update.message.chat_id,photo = 'https://i.dlpng.com/static/png/507790_preview.png')
  send_value(1)

def Turnoff(update, bot):
  update.message.reply_text("Light turned off ,value=0 sent to adafruit_io feed")
  bot.send_photo(chat_id = update.message.chat_id, photo='https://i.dlpng.com/static/png/7501809_preview.png')
  send_value(0)

def input_message(update, bot):
  text=update.message.text.upper()
  text=update.message.text
  if text == 'Turnon':
    send_value(1)
    update.message.reply_text("Light turned on,value=1 sent to adafruit_io feed")
    bot.send_photo( chat_id = update.message.chat_id,photo ='https://i.dlpng.com/static/png/507790_preview.png')
  elif text == 'Turnoff':
    send_value(0)
    update.message.reply_text("Light turned off,value=0 sent to adafruit_io feed")
    bot.send_photo( chat_id = update.message.chat_id, photo='https://i.dlpng.com/static/png/7501809_preview.png')

u = Updater('TOKEN')
dp = u.dispatcher
dp.add_handler(CommandHandler('start',start))
dp.add_handler(CommandHandler('Turnoff',Turnoff))
dp.add_handler(CommandHandler('Turnon',Turnon))
dp.add_handler(MessageHandler(Filters.text & (~Filters.command),input_message))
u.start_polling()
u.idle()
