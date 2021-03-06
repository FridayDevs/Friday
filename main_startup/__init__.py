# Copyright (C) 2020-2021 by DevsExpo@Github, < https://github.com/DevsExpo >.
#
# This file is part of < https://github.com/DevsExpo/FridayUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DevsExpo/blob/master/LICENSE >
#
# All rights reserved.

import logging
import os
import time
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from pyrogram import Client
from .config_var import Config

# Note StartUp Time - To Capture Uptime.
start_time = time.time()
friday_version = "V8.0 - ReBorn"

# Enable Logging For Pyrogram
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [FridayUB] - %(levelname)s - %(message)s",
)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("apscheduler").setLevel(logging.ERROR)


mongo_client = MongoClient(Config.MONGO_DB)

try:
    mongo_client.server_info()
except ConnectionFailure:
    logging.error("Invalid Mongo DB URL. Please Check Your Credentials! Friday is Exiting...")
    quit(1)


CMD_LIST = {}
XTRA_CMD_LIST = {}
sudo_id = Config.AFS

if not Config.STRINGSESSION:
    logging.info("No String Session Found! Daisy is Exiting!")
    quit(1)

if not Config.API_ID:
    logging.info("No Api-ID Found! Daisy is Exiting!")
    quit(1)

if not Config.API_HASH:
    logging.info("No ApiHash Found! Daisy is Exiting!")
    quit(1)
    
    


# Clients - Upto 4 Clients is Supported!
if Config.STRINGSESSION:
    Friday = Client(
        Config.STRINGSESSION, api_id=Config.API_ID, api_hash=Config.API_HASH, sleep_threshold=1800
    )
if Config.STRINGSESSION_2:
    Friday2 = Client(
        Config.STRINGSESSION_2, api_id=Config.API_ID, api_hash=Config.API_HASH, sleep_threshold=1800
    )
else:
    Friday2 = None
if Config.STRINGSESSION_3:
    Friday3 = Client(
        Config.Config.STRINGSESSION_3, api_id=Config.API_ID, api_hash=Config.API_HASH, sleep_threshold=1800
    )
else:
    Friday3 = None
if Config.STRINGSESSION_4:
    Friday4 = Client(
        Config.Config.STRINGSESSION_4, api_id=Config.API_ID, api_hash=Config.API_HASH, sleep_threshold=1800
    )
else:
    Friday4 = None

if Config.BOT_TOKEN:
    bot = Client(
        "MyAssistant",
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        bot_token=Config.BOT_TOKEN,
        sleep_threshold=1800
    )
else:
    bot = None
