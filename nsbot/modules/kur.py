from pyrogram import filters
from nsbot import bot

import requests
from bs4 import BeautifulSoup

def doviz():
    global USD, EUR, GBP
    res = requests.get("http://www.doviz.com")
    soup = BeautifulSoup(res.text.replace(",", "."), "lxml")
    rates = soup.findAll("span", {"class": "value"})
    USD = float(rates[1].text)
    EUR = float(rates[2].text)
    GBP = float(rates[3].text)
doviz()

@bot.on_message(filters.command("kur"))
async def kur(client, message):
    num = 1
    if len(message.command) != 1:
        num = int(message.text.replace("/kur ",""))
    if num == 1:
        await message.reply_text(f"USD = {USD:.2f} TL\nEUR = {EUR:.2f} TL\nGBP = {GBP:.2f} TL")
    else:
        await message.reply_text(f"{num} USD = {num*USD:.2f} TL\n{num} EUR = {num*EUR:.2f} TL\n{num} GBP = {num*GBP:.2f} TL")
