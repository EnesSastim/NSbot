from pyrogram import filters
from nsbot import bot

from cowpy import cow
import random

cows = [cow.Cowacter, cow.Moofasa, cow.Moose, cow.Mutilated, cow.Satanic,
        cow.Sheep, cow.Small]

@bot.on_message(filters.command("cowsay"))
async def cowsay(client, message):
    n = random.randint(0, len(cows)-1)

    text = "There is no Text!"
    if len(message.command) != 1:
        text = message.text.replace("/cowsay","")
    elif message.reply_to_message is not None:
        if message.reply_to_message.text is not None:
            text = message.reply_to_message.text

    cheese = cows[n]()
    await message.reply_text(f"`{cheese.milk(text).replace('`', '´')}`")
