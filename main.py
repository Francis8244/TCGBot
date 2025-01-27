import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot Ready!")

async def Load():
    print(f"{bot.user} has connected!")
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            cog_name = f'cogs.{filename[:-3]}'
            await bot.load_extension(cog_name)

async def main():
    async with bot:
        await Load()
        await bot.start(TOKEN)

asyncio.run(main())