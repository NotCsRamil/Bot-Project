import discord
import os
import asyncio
import random
import json
from discord.ext import commands, tasks
from itertools import cycle
from discord.ext import commands






client= commands.Bot(command_prefix = "&")
status = cycle(["Ghilli","Pokkiri","Vettaikaran","Kaavalan","Thuppaki","Katthi","Mersal","Sarkar","Bigil"])

@client.event
async def on_ready():
    changemovies.start()
    print(f"{client.user} has connected to discord...\n")

'''class Myclient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.author.bot:
            return
        await message.channel.send("vanakam")'''

    #await client.change_presence(status=discord.Status.idle, activity=discord.Game("Ghilli"))

#lvls

'''m = {}

@client.event
async def on_ready():
    global m
    with open("users.json", "r") as j:
        m = json.load(j)
        j.close()
    if len(m) == 0:
        m = {}
        for member in client.get_guild(754716663529734254).members:
            m[str(member.id)] = {"xp" : 0, "messageCountdown" : 0}
    print("ready")
    while True:
        try:
            for member in client.get_guild(754716663529734254).members:
                m[str(member.id)]["messageCountdown"] -= 1
        except:
            pass
        await asyncio.sleep(1)

@client.event
async def on_message(message):
    global m
    if message.content == "&stop" and message.author.id == 677071327265423360:
        with open("users.json", "w") as j:
            j.write( json.dumps(m) )
            j.close()
        await client.close()
    elif message.content == "&xp":
        await message.channel.send( str(m[str(message.author.id)]["xp"]) )
    elif message.author != client.user:
        if m[str(message.author.id)]["messageCountdown"] <= 0:
            m[str(message.author.id)]["xp"] += 10
            m[str(message.author.id)]["messageCountdown"] = 10

@client.event
async def on_member_join(member):
    m[str(member.id)] = {"xp" : 0, "messageCountdown" : 0}'''




    


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

#fantasy team
@client.command()
async def vijays_11(ctx):
    ramil = ['https://cdn.discordapp.com/attachments/751422342709903370/767777080653250580/Screenshot_61.png']
             
    await ctx.send(random.choice(ramil))
@client.command()
async def rounaks_11(ctx):
    rounak = ['https://cdn.discordapp.com/attachments/751422342709903370/767979322584727562/team_2.png']
             
    await ctx.send(random.choice(rounak))
@client.command()
async def abizois_11(ctx):
    abizoi = ['https://cdn.discordapp.com/attachments/674567305291890701/768118602690854972/unknown.png']
             
    await ctx.send(random.choice(abizoi))
@client.command()
async def ayaans_11(ctx):
    ayaan = ['https://cdn.discordapp.com/attachments/751422342709903370/768106808958255134/Screenshot_20201020-174200_Chrome.jpg']
             
    await ctx.send(random.choice(ayaan))



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

#admin commands
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await ctx.channel.send(
        "Command Executed BOSS"
        f"{member.mention} has been **kicked**")
    await member.kick(reason=reason)

@client.command()
async def poda(ctx):
    if ctx.message.author.discriminator == '6012' :
        await ctx.send('Ok BOSS <a:polish_cow:767665553187012639>')
        await client.logout()
    else :
        await ctx.send('You messed With the Wrong Person')
'''client = Myclient()'''                     
client.run("NzY2MjY0Njc1MzQ4MTE5NTUy.X4g1lw.aisadbOT5dQ4eGAXLwa5qgmmZ10")



