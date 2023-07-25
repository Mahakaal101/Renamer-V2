import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5822225258:AAHzJCvixTXkRIvnTaIwaF0SNcQtXTz8Keo")

API_ID = int(os.environ.get("API_ID", "24237617"))

API_HASH = os.environ.get("API_HASH", "8ec32b4085f1e3cf56c34a6afe1cc590")

STRING = os.environ.get("STRING", "BQFx1jEAqxjYofT4TsIc1kjkgYzfnsvcUUzLyPTVPEtEGZMTl1lhzIpXBWnTIDkuhSuWJGlhEGGpgFI89_NhlUWt9Hbd8eCLBJ0CW48YtUx6UrP6HeVNOHYEsOC2PCRJB_tlwi6Gwjyp0VW0pfp4qavefwuzOgFgJF20ve_lLgsfbNs5nz5jOXPmGIdKvwnNwGOAlYhchrhoixYjnSIo5kKLYG98okb5Sl4yFADKKd6J1Lx-bDHeX3eQ9_ZArcuLBZdRWTpZ56wnFbq2zs_cXig-qRjHxHU564yfX31XiB-4wOgg-nehylp67QI_9bcDq2AEgMPUa_rCul6y2otKr038QqEzBwAAAAF7vgGsAA")


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
