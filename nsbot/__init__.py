from pyrogram import Client
#from pyrogram.errors import BadRequest, Forbidden, FloodWait, RPCError
from dotenv import load_dotenv
from logging import DEBUG, INFO, basicConfig, getLogger

import os
import sys

basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=INFO)

load_dotenv("config.env")

LOGS = getLogger(__name__)

# Checking if the config.env file is edited correctly
CONFIG_CHECK = os.environ.get("__Remove_This_Line__") or None
if CONFIG_CHECK:
    LOGS.error("Please remove the first line of config.env")
    sys.exit(1)

API_KEY = os.environ.get("API_KEY") or None
if not API_KEY:
    LOGS.error("API Key is not set! Check your config.env!")
    sys.exit(1)

API_HASH = os.environ.get("API_HASH") or None
if not API_HASH:
    LOGS.error("API Hash is not set! Check your config.env!")
    sys.exit(1)

BOT_TOKEN = os.environ.get("BOT_TOKEN") or None
if not BOT_TOKEN:
    LOGS.error("Bot Token is not set! Check your config.env!")
    sys.exit(1)

bot = Client(
    "nsbot",
    bot_token=BOT_TOKEN,
    api_id=API_KEY,
    api_hash=API_HASH
)
