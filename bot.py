import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6266474006:AAGr5-dbhpUd8Afeu6_GJf6Cri3vUOh3-b8")

API_ID = int(os.environ.get("API_ID", "26305247"))

API_HASH = os.environ.get("API_HASH", "20ca7e6687c281e11782856c7efd0ff7")

STRING = os.environ.get("STRING", "BQBVwpItoDnVyhwuKE9raKXfU9_ttPKmeVXiMAzcDQup8DDidlYLWhAHGQ-DFBtlpUp3r1MN6PVc10qw3S91JMcK71Vz7Uf8OhXJ1u0RLUtBHbWr0nWXrdfFfGZbH5nIJQnCio1SX6I-lNw_Mf-wVdIOIVv3Jk7ilc6_yh37mNcK07z6Lj9B2nDuzN6Xj0P9EDIXw6q2ul8mD00u7ztHRHwyDAi-r6TjrA_7Wo4EuhiaB11n0kE2QUk-KAMNIY1VP0n2DG0VLw6fyXnn5zwDh7OAZStK2wmyHrHhKEIcZlHqd-RUqFuAfXWgqLs01LtpeF9hqGUqUWH8JzVobDroLs21AAAAATMiN8EA")



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
