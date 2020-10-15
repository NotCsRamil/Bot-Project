import discord
import random
from discord.ext import commands

client= commands.Bot(command_prefix = "&")

@client.event
async def on_ready():
    print("good to go")
    
@client.command()#ep3b
async def ping(ctx):
    await ctx.send(f'pong! {round(client.latency*1000)}ms')

@client.command(aliases=["8ball","test"])
async def _8ball(ctx,*, question):
    responses = [
        "It is certain.",
"It is decidedly so.",
"Without a doubt.",
"Yes - definitely.",
"You may rely on it.",
"As I see it, yes.",
"Most likely.",
"Outlook good.",
"Yes.",
"Signs point to yes.",
"Reply hazy, try again.",
"Ask again later.",
"Better not tell you now.",
"Cannot predict now.",
"Concentrate and ask again.",
"Don't count on it.",
"My reply is no.",
"My sources say no.",
"Outlook not so good."
"Very doubtful."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
        


    
client.run("NzY2MjY0Njc1MzQ4MTE5NTUy.X4g1lw.uXGf8nniNL4-9H2q1bd947LgZj8")

