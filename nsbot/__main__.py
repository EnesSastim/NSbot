from importlib import import_module
import asyncio
import os

from pyrogram import idle
from nsbot import LOGS, bot
from nsbot.modules import ALL_MODULES, module_names

async def main():
    await bot.start()
    LOGS.info("NSbot is running! Test by typing /start.")
    LOGS.info("Loaded Modules: %s", module_names)
    await idle()


for module_name in ALL_MODULES:
    import_module(f"nsbot.modules.{module_name}")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
