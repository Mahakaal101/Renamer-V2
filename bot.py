import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6266474006:AAG3V0X_-k_6dNI0QHHkP42PS6daAiODVKw")

API_ID = int(os.environ.get("API_ID", "26305247"))

API_HASH = os.environ.get("API_HASH", "20ca7e6687c281e11782856c7efd0ff7")

STRING = os.environ.get("STRING", "BQAelg_pvzw_veEjEpzL0AdWM4H4_VgbSg5qckh1vpmqjnnqGOZ-zSL_mqSpfPj1yEURAGZwphmNPQrpixzVZ0kqHp7ncKz4ixfzLE199ov10q14bLlHI8pgG9VWMH9gRi8Cdoq-xh2euP7BA36kIxTQeGHUQABo_WttQMQJF6dfCF_d5k9qv5hXoWzbZfPwmf-EUUAhYd7dwTPG2vCSVjp_daWzdGGOgG7AJksEMQpoSQRhbJgG6Qpxz1nu67X4VCndBFGkjGHsUkRCLDb-iUkbIUvvZQCRYCpkZjS8q67KPT0etl2u2BpbfRXLFRkBBjGkiksVUoam18IoLLR16zaEAAAAATMiN8EA")



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
