from pyrogram import filters
from nsbot import bot

import random

startlist = ["Hello!", "I'm Up!", "I'm Running!"]


@bot.on_message(filters.command("start"))
async def start(client, message):
    n = random.randint(0, len(startlist)-1)
    await message.reply_text(startlist[n])
