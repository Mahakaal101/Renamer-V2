import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5552531861:AAFIAB4cR8-OZMuQxR3Wi4IgBi5mTX_gfIs")

API_ID = int(os.environ.get("API_ID", "23560088"))

API_HASH = os.environ.get("API_HASH", "999c01704d5c417749a98f4b8785fe88")

STRING = os.environ.get("STRING", "BQFnf5gAxhqfyq-cfzeiczSZ_EgOvLzWVHoqikAq61uIh6QJR0tdn-h7EWp7sdE5aCDgj3_sLr5taSq_UtJzafLUb7r1d819aSP92l9nSiiTxhi1cJ-a_Sxx0MvLdI1Yu4bQI5HORC3hoMcD6Nl4SxPDj5OCM2knrtBYipKpWc2e5AooG_-5N6R0CtWtFGZYljna6tXbo-MqY0oNtUPg9EYPWjCZWYFcHnsOQymWQ2QBduzE7HOgvNEuAyrnTU2P6epv638F47eVdgP3hcF_uK3m0elHQe99PL3SlWqOQJPwzWbsLhjBgH9am4uWrIcg4a2jWxNSrwKATW97H1tJxFBPUoZs0wAAAABvJ4dUAA")



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
