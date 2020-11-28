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

def start(update, context):
  update.reply_text("/Turnon : To turn on the light /Turnoff : To turn off the light")

def Turnon(update, context):
  context.bot.send_message(chat_id=update.effective_chat.id, text="Light turned on")
  context.bot.send_photo(chat_id=update.effective_chat.id,photo='https://i.dlpng.com/static/png/507790_preview.png')
  send_value(1)

def Turnoff(update, context):
  context.bot.send_message(chat_id=update.effective_chat.id, text="Light turned off")
  context.bot.send_photo(chat_id=update.effective_chat.id,photo='https://i.dlpng.com/static/png/7501809_preview.png')
  send_value(0)

def input_message(update, context):
  text=update.message.text.upper()
  text=update.message.text
  if text == 'Turnon':
    send_value(1)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Light turned on")
    context.bot.send_photo(chat_id=update.effective_chat.id,photo='https://i.dlpng.com/static/png/507790_preview.png')
  elif text == 'Turnoff':
    send_value(0)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Light turned off")
    context.bot.send_photo(chat_id=update.effective_chat.id,photo='https://i.dlpng.com/static/png/7501809_preview.png')
updater=Updater(TOKEN,use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('turnoff',Turnoff))
dispatcher.add_handler(CommandHandler('turnon',Turnon))
dispatcher.add_handler(CommandHandler('start',start))
dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command),input_message))
updater.start_polling()
updater.idle()
