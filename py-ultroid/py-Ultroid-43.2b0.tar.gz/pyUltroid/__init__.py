# Ultroid - UserBot
# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

from datetime import datetime as dt

from .connections import LOGS, client_connection, redis_connection

LOGS = LOGS

START_TIME = dt.now()

udB = redis_connection()

ultroid_bot = client_connection()

if not udB.get("HNDLR"):
    udB.set("HNDLR", ".")
HNDLR = udB.get("HNDLR")
if not udB.get("SUDO"):
    udB.set("SUDO", "False")

if not udB.get("SUDOS"):
    udB.set("SUDOS", "777000")

if not udB.get("BLACKLIST_CHATS"):
    udB.set("BLACKLIST_CHATS", "[]")
