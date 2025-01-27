from pokemontcgsdk import Card
from pokemontcgsdk import Set
from pokemontcgsdk import Type
from pokemontcgsdk import Supertype
from pokemontcgsdk import Subtype
from pokemontcgsdk import Rarity
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("POKEMONTCG_IO_API_KEY")

class Gamble(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name_} is online!")

    @commands.command()
    async def gamble(self, ctx):
        card = Card.find('xy1-1')
        await ctx.send(f"Card Name: {card.name}")

async def setup(bot):
    await bot.add_cog(Gamble(bot))