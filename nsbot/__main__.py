from importlib import import_module
import os
import sys

from nsbot import LOGS, bot
from nsbot.modules import ALL_MODULES

for module_name in ALL_MODULES:
    import_module(f"nsbot.modules.{module_name}")

LOGS.info(
    "NSbot is running! Test by typing /start."
)

bot.run()
