from pyrogram import filters
from nsbot import bot, OWNER_ID, SUDO_USERS

import random

startlist = ["Hello", "I'm Up", "I'm Running"]


@bot.on_message(filters.command("start"))
async def start(client, message):
    id = message.from_user.id
    n = random.randint(0, len(startlist)-1)
    if id == OWNER_ID:
        await message.reply_text(startlist[n]+", Owner!")
    elif id in SUDO_USERS:
        await message.reply_text(startlist[n]+", Sudo User!")
    else:
        await message.reply_text(startlist[n]+"!")
