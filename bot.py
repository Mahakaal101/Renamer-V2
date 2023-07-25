import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5822225258:AAHzJCvixTXkRIvnTaIwaF0SNcQtXTz8Keo")

API_ID = int(os.environ.get("API_ID", "24237617"))

API_HASH = os.environ.get("API_HASH", "8ec32b4085f1e3cf56c34a6afe1cc590")

STRING = os.environ.get("STRING", "")

bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
