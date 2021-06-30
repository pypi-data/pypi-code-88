# DONT KANG. OTHERWISE GET READY FOR COPYRIGHT STRIKE
# MADE BY GODBOYX (PERRY_XD), AMAN PANDEY

from GODBOY import bot
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient
from GODBOY.variables import Var
from GODBOY.utils import load_module
from GODBOY.utils import start_assistant
from GODBOY import LOAD_PLUG, BOTLOG_CHATID, LOGS
from pathlib import Path
import asyncio
import telethon.utils



                    
async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me() 
    bot.uid = telethon.utils.get_peer_id(bot.me)



if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Userbot Is Starting With Telethon")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
    else:
        bot.start()
import glob
path = 'assistant/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        start_assistant(shortname.replace(".py", ""))   



import glob

path = 'plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))



print("Userbot Is Deployed With Success Sign")



if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
    
