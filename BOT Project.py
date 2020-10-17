import discord
import os
import asyncio
import tracemalloc
import random
from discord.ext import commands, tasks
from itertools import cycle

tracemalloc.start()

client= commands.Bot(command_prefix = "&")
status = cycle(["Ghilli","Pokkiri","Vettaikaran","Kaavalan","Thuppaki","Katthi","Mersal","Sarkar","Bigil"])

@client.event
async def on_ready():
    changemovies.start()
    print(f"{client.user} has connected to discord...\n")

    #await client.change_presence(status=discord.Status.idle, activity=discord.Game("Ghilli"))


class MyContext(commands.Context):
    async def tick(self, value):
        # reacts to the message with an emoji
        # depending on whether value is True or False
        # if its True, it'll add a green check mark
        # otherwise, it'll add a red cross mark
        emoji = '\N{WHITE HEAVY CHECK MARK}' if value else '\N{CROSS MARK}'
        try:
            # this will react to the command author's message
            await self.message.add_reaction(emoji)
        except discord.HTTPException:
            # sometimes errors occur during this, for example
            # maybe you dont have permission to do that
            # we dont mind, so we can just ignore them
            pass

#ping command   
@client.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(client.latency*1000)}ms<a:cat_vibing:753973817608634468>')

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

#wrong commands
@client.event
async def on_command_error(ctx , error):
    await ctx.send(f'Thendi wrong command {ctx.message.author.mention}')
    await ctx.send(error)

'''#guess game
@client.command()
async def guess(message, number: int):
    value = random.randint(1, 6)
    if number == value:
        await message.add_reaction(emoji = "✅")
    else:
        await message.add_reaction(emoji = "❌")'''

#vijays lines
@client.command()
async def punch(ctx,arg):
    punchs = {

    'ayaan' : 'Nee Pozhapukku Daan Rowdy. Naa Porandadhulendhe Rowdy.',
    'rounak' : 'Namma Paechu Mattum Daan Silent Ah Irukum, Aana Adi Saravedi.',
    'ramanan' : 'Oru Vaati Mudivu Panta, Yen Pecha Naane Kekka Maaten.',
    'harshal' : 'Nee padicha school la na headmaster da.',
    'ramil' : 'All Arealayum Aiyaa Ghilli Da.',
    'vivek' : 'I’m Waiting.',
    'abishai' : 'Saami Munaadi Daan Shaanthama Pesuven. Sakaada Munaadi Ila.',}
    await ctx.send(punchs.get(arg.lower(),"Taap ana paare <:abeysaale:731486907208433724>"),tts = True)

@client.command()
async def poda(ctx):
    if ctx.message.author.discriminator == '6012' :
        await ctx.send('Ok BOSS')
        await client.logout()
    else :
        await ctx.send('You messed With the Wrong Person')
