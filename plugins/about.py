import os 
from pyrogram import Client, filters
token = os.environ.get('TOKEN','5552531861:AAFIAB4cR8-OZMuQxR3Wi4IgBi5mTX_gfIs')
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user

from helper.progress import humanbytes

@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"Origional BOT :- <a href='https://t.me/renamerprov2_bot'>Gangster Baby</a>\nCreater :- <a href='https://t.me/ajak4405'>🦋Amit🦋</a>\nLanguage :- Python3\nLibrary :- Pyrogram 2.0\nServer :- UBUNTU\nTotal Renamed File :- {total_rename}\nTotal Size Renamed :- {humanbytes(int(total_size))} \n\n Thank you **<a href='https://t.me/ajak4405'>Amit</a>** for your hard work \n\n❤️ we love you <a href='https://t.me/ajak4405'>**LazyDeveloper**</a> ❤️",quote=True)
