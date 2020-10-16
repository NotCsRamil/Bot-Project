import discord
import random
from discord.ext import commands, tasks
from itertools import cycle

client= commands.Bot(command_prefix = "&")
status = cycle(["Ghilli","Pokkiri","Vettaikaran","Kaavalan","Thuppaki","Katthi","Mersal","Sarkar","Bigil"])

@client.event
async def on_ready():
    changemovies.start()
    print("good to go")
    #await client.change_presence(status=discord.Status.idle, activity=discord.Game("Ghilli"))

#ping command   
@client.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(client.latency*1000)}ms<:abeysaale:731486907208433724>')

#Fortune teller
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
"Better not to tell you now.",
"Cannot predict now.",
"Concentrate and ask again.",
"Don't count on it.",
"My reply is no.",
"My sources say no.",
"Outlook not so good."
"Very doubtful."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

#Delete Message
@client.command()
async def clear(ctx, amount=3):
    await ctx.channel.purge(limit=amount)


#Show Avatars        
@client.command()
async def moonji(ctx, user: discord.User = None):
    if user==None:
        user = ctx.message.author
    await ctx.send(user.avatar_url_as())


#movie cycle
@tasks.loop(seconds=3)
async def changemovies():
    await client.change_presence(activity=discord.Game(next(status)))
    


    
client.run("token")

