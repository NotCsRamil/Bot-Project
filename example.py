import discord
from discord.ext import commands

class Example(commands.Cog):

    def _init_(self, client):
        self.client = client

    @commands.Cog.listener()#events
    async def on_ready(self):
        print("Bot is awake")

    @commands.command()#commands
    async def ping(self, ctx):
        await ctx.send("pong!")

def setup(client):
    client.add_cog(Example(client))
