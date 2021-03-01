import keep_alive
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")


bot = commands.Bot(command_prefix="Tu prefix ale niejest puki co potrzebny")
client = discord.Client()


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    
    if message.content.startswith('TU WPISZ KOMENDE'):
        await message.channel.send('A TU CO MA ODPISAĆ BOT')
                          
keep_alive.keep_alive()
bot.run(os.getenv("TOKEN"))
