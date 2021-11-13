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

EMOJIS = [
    "😂", "😂", "👌", "✌", "💞", "👍", "👌", "💯", "🎶", "👀", "😂",
    "👓", "👏", "👐", "🍕", "💥", "🍴", "💦", "💦", "🍑", "🍆", "😩",
    "😏", "👉👌", "👀", "👅", "😩", "🚰"]

@bot.on_message(filters.command("cp"))
async def copypasta(client, message):
    """Copypasta the famous meme"""
    text = "Give me some Text!"
    if len(message.command) != 1:
        text = message.text.replace("/cp","")
    elif message.reply_to_message is not None:
        if message.reply_to_message.text is not None:
            text = str(message.reply_to_message.text)

    reply_text = random.choice(EMOJIS)
    # choose a random character in the message to be substituted with 🅱️
    b_char = random.choice(text).lower()
    for i in text:
        if i == " ":
            reply_text += random.choice(EMOJIS)
        elif i in EMOJIS:
            reply_text += i
            reply_text += random.choice(EMOJIS)
        elif i.lower() == b_char:
            reply_text += "🅱️"
        else:
            if bool(random.getrandbits(1)):
                reply_text += i.upper()
            else:
                reply_text += i.lower()
    reply_text += random.choice(EMOJIS)
    await message.reply_text(reply_text)
