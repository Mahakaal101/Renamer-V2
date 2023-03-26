import os 
from pyrogram import Client, filters
token = os.environ.get('TOKEN','6266474006:AAG3V0X_-k_6dNI0QHHkP42PS6daAiODVKw')
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user

from helper.progress import humanbytes

@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"Origional BOT :- <a href='https://t.me/https://t.me/Mdisk_downloader_rebot'>Gangster Baby</a>\nCreater :- <a href='https://t.me/ajak4405'>🦋Amit🦋</a>\nLanguage :- Python3\nLibrary :- Pyrogram 2.0\nServer :- UBUNTU\nTotal Renamed File :- {total_rename}\nTotal Size Renamed :- {humanbytes(int(total_size))} \n\n Thank you **<a href='https://t.me/ajak4405'>Amit</a>** for your hard work \n\n❤️ we love you <a href='https://t.me/ajak4405'>**LazyDeveloper**</a> ❤️",quote=True)
