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
  start_message='''
  /Turnoff or 'Turn off':To turn off the light 
  /Turnon or 'Turn on'  :To turn on the light 
  '''
  context.bot.send_message(chat_id=update.effective_chat.id, text=start_message)
def Turnon(update, context):
  context.bot.send_message(chat_id=update.effective_chat.id, text="Light turned on, value sent to adafruit-io feed")
  context.bot.send_photo(chat_id=update.effective_chat.id,photo='https://i.dlpng.com/static/png/507790_preview.png')
  send_value(1)

def Turnoff(update, context):
  context.bot.send_message(chat_id=update.effective_chat.id, text="Light turned, value sent to adafruit-io feed")
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
u =Updater(TOKEN,use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler('turnoff',Turnoff))
dp.add_handler(CommandHandler('turnon',Turnon))
dp.add_handler(CommandHandler('start',start))
dp.add_handler(MessageHandler(Filters.text & (~Filters.command),input_message))
u.start_polling()
u.idle()
 
