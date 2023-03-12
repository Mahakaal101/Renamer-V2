import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5552531861:AAFIAB4cR8-OZMuQxR3Wi4IgBi5mTX_gfIs")

API_ID = int(os.environ.get("API_ID", "23560088"))

API_HASH = os.environ.get("API_HASH", "999c01704d5c417749a98f4b8785fe88")

STRING = os.environ.get("STRING", "BQFnf5gAjWnX9Igl0mtjwCwKZkiW6J-nvazNnoq1iV-km7dyJXsXSzPDotfl3E92wCBMddsRZjeIsMSenxhCOUyJnrTC986F3jkrtw66Ocaq41l-AZS22gHkEn521p-XFqs94uJ7Gx-rxP7IZ_5d1fmNIXVFbn6HDPWS0v_RbN_-btx3PSIE5dluJNbpkrHuvWuh3491VWhfhb-ISoOjF-HL-XCvlMGyoMgkDeZXH4HlIMFKIN8YDpbUcfF7PBuVwVotAfUp_xn7njY4hHTzqDIFP3xKabASXSu975JQd2BdYSb6NcDHLPYsKUCd1PsHAVaRz1jhrw2zMB8gPNLL-R-_kO2ygQAAAABvJ4dUAA")



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
