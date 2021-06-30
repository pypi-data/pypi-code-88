# Ultroid - UserBot
# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

import os
import time
from logging import INFO, FileHandler, StreamHandler, basicConfig, getLogger

from pyrogram import Client
from pytgcalls import PyLogs, PyTgCalls
from redis import StrictRedis
from telethon import TelegramClient
from telethon.errors.rpcerrorlist import (
    ApiIdInvalidError,
    AuthKeyDuplicatedError,
    PhoneNumberInvalidError,
)
from telethon.sessions import StringSession

from .dB.database import Var

LOGS = getLogger("pyUltroid")

if os.path.exists("ultroid.log"):
    try:
        os.remove("ultroid.log")
    except BaseException:
        pass

basicConfig(
    format="%(asctime)s || %(name)s [%(levelname)s] - %(message)s",
    level=INFO,
    datefmt="%m/%d/%Y, %H:%M:%S",
    handlers=[FileHandler("ultroid.log"), StreamHandler()],
)

LOGS.info(
    """
                -----------------------------------
                        Starting Deployment
                -----------------------------------
"""
)


def connect_redis():
    err = ""
    if ":" not in Var.REDIS_URI:
        err += "\nWrong REDIS_URI. Quitting...\n"
    if "/" in Var.REDIS_URI:
        err += "Your REDIS_URI should start with redis.xxx. Quitting...\n"
    if " " in Var.REDIS_URI:
        err += "Remove space from REDIS_URI\n"
    if " " in Var.REDIS_PASSWORD:
        err += "Remove space from REDIS_PASSWORD\n"
    if "\n" in Var.REDIS_URI:
        err += "Remove new-line from REDIS_URI\n"
    if "\n" in Var.REDIS_PASSWORD:
        err += "Remove new-line from REDIS_PASSWORD\n"
    if err != "":
        LOGS.info(err)
        exit(1)
    redis_info = Var.REDIS_URI.split(":")
    DB = StrictRedis(
        host=redis_info[0],
        port=redis_info[1],
        password=Var.REDIS_PASSWORD,
        charset="utf-8",
        decode_responses=True,
    )
    LOGS.info("Getting Connection With Redis Database")
    return DB


def redis_connection():
    our_db = connect_redis()
    time.sleep(6)
    try:
        our_db.ping()
    except BaseException:
        connected = False
        LOGS.info("Can't connect to Redis Database.... Restarting....")
        for x in range(1, 6):
            our_db = connect_redis()
            time.sleep(5)
            try:
                if our_db.ping():
                    connected = True
                    break
            except BaseException as conn:
                LOGS.info(
                    f"{type(conn)}\nConnection Failed ...  Trying To Reconnect {x}/5 .."
                )
        if not connected:
            LOGS.info("Redis Connection Failed.....")
            exit(1)
        else:
            LOGS.info("Reconnected To Redis Server Succesfully")
    LOGS.info("Succesfully Established Connection With Redis DataBase.")
    return our_db


def session_file():
    if os.path.exists("client-session.session"):
        _session = "client-session"
    elif Var.SESSION:
        _session = StringSession(Var.SESSION)
    else:
        LOGS.info("No String Session found. Quitting...")
        exit(1)
    return _session


def client_connection():
    try:
        client = TelegramClient(session_file(), Var.API_ID, Var.API_HASH)
    except AuthKeyDuplicatedError or PhoneNumberInvalidError or EOFError:
        LOGS.info(
            "String Session Expired. Please Create New String Session. Quitting..."
        )
        exit(1)
    except ApiIdInvalidError:
        LOGS.info(
            "API_ID and API_HASH combination invalid. Please Re-Check. Quitting..."
        )
        exit(1)
    except Exception as ap:
        LOGS.info(f"ERROR - {ap}")
        exit(1)
    return client


def vc_connection(udB):
    VC_SESSION = udB.get("VC_SESSION") or Var.VC_SESSION
    if VC_SESSION:
        try:
            vcasst = Client(
                ":memory:",
                api_id=Var.API_ID,
                api_hash=Var.API_HASH,
                bot_token=udB.get("BOT_TOKEN"),
            )
            vcClient = Client(VC_SESSION, api_id=Var.API_ID, api_hash=Var.API_HASH)
            CallsClient = PyTgCalls(vcClient, log_mode=PyLogs.ultra_verbose)
            return vcasst, vcClient, CallsClient
        except Exception as er:
            LOGS.info(str(er))
    return None, None, None
