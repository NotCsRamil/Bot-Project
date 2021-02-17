import discord
import praw
import os
import asyncio
import random
import platform
import datetime
import time
from discord import Embed, Color
from discord.ext import commands, tasks
from itertools import cycle
from discord.ext import commands
from discord.utils import get
from pathlib import Path


intents = discord.Intents(
messages=True, guilds=True, reactions=True, members=True)

client = commands.Bot(command_prefix='&', intents = intents)



filtered_words = ["vigae","VIGAE","Vigae"]


client.sniped_messages = {}
#status = cycle(["Ghilli","Pokkiri","Vettaikaran","Kaavalan","Thuppaki","Katthi","Mersal","Sarkar","Bigil"])

@client.event
async def on_message(msg):
    for word in filtered_words:
        if word in msg.content:
            await msg.delete()

    await client.process_commands(msg)


@client.command()
async def stats(ctx, member: discord.Member):
    roles = [role for role in member.roles]

    embed = discord.Embed(color=member.color, timestamp=datetime.datetime.utcnow())

    embed.set_author(name=f"{member}", icon_url=member.avatar_url)

    embed.set_image(url=member.avatar_url)

    embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name="Joined Discord on:", value=member.created_at.strftime("%a, %d %B, %Y, %I:%M %p UTC"), inline=False)

    embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))

    embed.add_field(name="Top role:", value=member.top_role.mention)

    embed.add_field(name="Bot?", value=member.bot)
    embed.set_footer(text=f"Requested By: {ctx.author.name}")

    await ctx.send(embed=embed)

@client.event
async def on_ready():
    #changemovies.start()
    print(f"{client.user} has connected to discord...\n")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Vaathi Raid"))
    #time = datetime.datetime.now()
    #print("wiki search online at {}".format(time))

    client.reaction_roles = []



        
        
  

  

reddit = praw.Reddit(client_id = "XbpGg2yOepX2ow",
                     client_secret = "gf2mKU5HUV8f62E4lXpRPnZpw-eufA",
                     username = "SerialKiller605",
                     password = "Dellg3@2020",
                     user_agent = "pythonpraw",
                     check_for_async=False
                     
                     )
@client.command()
async def meme(ctx,subred = "memes"):
    """
    gets memes from r\memes.
    """
    
    
    subreddit = reddit.subreddit("memes")
    all_subs = []

    hot = subreddit.hot(limit = 200)
    

    for submission in hot:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    url = random_sub.url

    em = discord.Embed(title = name)
    em.set_image(url= url)

    await ctx.send(embed= em)


@client.command()
async def pc(ctx,subred = "pcmasterrace"):

    """
    gets builds,memes from r\pcmasterrace.
    """

    


    subreddit = reddit.subreddit("pcmasterrace")
    all_subs = []

    hot = subreddit.hot(limit = 200)
    

    for submission in hot:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    url = random_sub.url

    em = discord.Embed(title = name)
    em.set_image(url= url)

    await ctx.send(embed= em)

@client.command()
async def amongus(ctx,subred = "AmongUs"):

    """
    gets amongus memes from r\Amongus.
    """
    subreddit = reddit.subreddit("AmongUs")
    all_subs = []

    hot = subreddit.hot(limit = 200)
    

    for submission in hot:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    url = random_sub.url

    em = discord.Embed(title = name)
    em.set_image(url= url)

    await ctx.send(embed= em)

@client.command()
async def warn(ctx, member : discord.Member, *, reason=None):
    embed = Embed(color=discord.Color.gold())
    embed.set_footer(text=f"Timestamp: {time.ctime()}\nInvoked by {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.add_field(name=f"WARNING!!",
                        value=f"{member.mention} you got a warn in the server from {ctx.author.mention} for the following reason:\n**{reason}**.")

    await ctx.send(embed=embed)




  
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
@commands.has_permissions(administrator=True)
@client.command(aliases=["redcard"])
async def kick(ctx, member : discord.Member, *, reason=None):
    await ctx.channel.send(
        "I see you want a free **Kick**. Have one!"
 
        f"{member.mention}")
    await member.kick(reason=reason)


@commands.has_permissions(administrator=True)
@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await ctx.channel.send(
        "I see you want a free **Ban**. Have one!"
 
        f"{member.mention}")
    await member.ban(reason=reason)


    
'''@client.event
async def on_member_join(member):
    autorole = discord.utils.get(member.guild.roles, name = 'Barca')
    await ctx.add_roles(autorole)'''

@client.command()
async def echo(ctx, *, message=None):
    """
    repeats back the user words.
    """
    message = message or "Please provide the message to be repeated."
    await ctx.message.delete()
    await ctx.send(message)


#ramanan server
@commands.has_permissions(administrator=True)
@client.command(aliases=["yellowcard"])
async def mute(ctx, member : discord.Member, *, reason=None):
        mute_role = discord.utils.get(ctx.guild.roles, name='Mute')
        await member.add_roles(mute_role, reason=reason)
        await ctx.channel.send("Command Executed BOSS "
        f"{member.mention} has been **muted**")

@commands.has_permissions(administrator=True)
@client.command()
async def unmute(ctx, member : discord.Member, *, reason=None):
    mute_role = discord.utils.get(ctx.guild.roles, name='Mute')
    await member.remove_roles(mute_role)
    await ctx.channel.send(f"{member.mention} has been **unmuted**")



'''@client.event
async def on_member_join(member):
    role = get(member.guild.roles, name="Gamer")
    await member.add_roles(role)
    print(f"{member} was given {role}")'''

'''@client.command()
async def addrole(ctx, role: discord.Role, member: discord.Member):
    if ctx.author.guild_permissions.administrator:
        await member.add_roles(role)
        await ctx.send(f"{member.mention} role alloted")

@client.command()
async def remove(ctx, role: discord.Role, member: discord.Member):
    if ctx.author.guild_permissions.administrator:
        await member.remove_roles(role)
        await ctx.send(f"{member.mention} role removed")'''



#role-reaction-abizoi-server
@client.event
async def on_raw_reaction_add(payload):
    guild = client.get_guild(payload.guild_id)
    member = get(guild.members, id=payload.user_id)
    # channel and message IDs should be integer:
    if payload.channel_id == 804255122271633409 and payload.message_id == 804295191942529094:
        if str(payload.emoji) == "<:Messirve:801506247571406850>":
            role = get(payload.member.guild.roles, name='Barca')

        elif str(payload.emoji) == "<:AmongUsDead:758633347059548211>":
            role = get(payload.member.guild.roles, name='AMONG US')

        elif str(payload.emoji) == "<:yellowglassdude:779372876699664435>":
            role = get(payload.member.guild.roles, name='Bayern')

         
        if role is not None:
            await payload.member.add_roles(role)
            print(f"Assigned {member} to {role}.")

        else:
            role = discord.utils.get(guild.roles, name=payload.emoji)

@client.event
async def on_raw_reaction_remove(payload):
    if payload.channel_id == 804255122271633409 and payload.message_id == 804295191942529094:
        if str(payload.emoji) == "<:Messirve:801506247571406850>":
            guild = client.get_guild(payload.guild_id)
            member = guild.get_member(payload.user_id)
            role = get(guild.roles, name='Barca')
            await member.remove_roles(role)
            print(f"Removed {role} from {member}.")
        elif str(payload.emoji) == "<:AmongUsDead:758633347059548211>":
            guild = client.get_guild(payload.guild_id)
            member = guild.get_member(payload.user_id)
            role = get(guild.roles, name='AMONG US')
            await member.remove_roles(role)
            print(f"Removed {role} from {member}.")
        elif str(payload.emoji) == "<:yellowglassdude:779372876699664435>":
            guild = client.get_guild(payload.guild_id)
            member = guild.get_member(payload.user_id)
            role = get(guild.roles, name='Bayern')
            await member.remove_roles(role)
            print(f"Removed {role} from {member}.")


@commands.has_permissions(administrator=True)
@client.command(aliases=['purge','clear','b'])
async def shoot(ctx, amount=3):
    await ctx.channel.purge(limit=amount)

@client.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(client.latency*1000)}ms<:Messirve:801506247571406850>')

#TTT

player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@client.command()
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
    else:
        await ctx.send("A game is already in progress! Finish it before starting a new one.")

@client.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:":
                board[pos - 1] = mark
                count += 1

                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                if gameOver:
                    await ctx.send(mark + " wins!")
                elif count >= 9:
                    await ctx.send("It's a tie!")

                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
        else:
            await ctx.send("It is not your turn.")
    else:
        await ctx.send("Please start a new game using the &tictactoe command.")


@client.command()
async def end(ctx):
  global gameOver
  if not gameOver:
    gameOver = True
    await ctx.send("Stopping current game...")
  else:
    await ctx.send("There is currently no game running!")





def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 2 players for this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping players .")

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer.")

#server info

@client.command()
async def server(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=name + " Server Information",
        description=description,
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)
    

    await ctx.send(embed=embed)

#send DMS

@client.command()
async def dm(ctx, member: discord.Member, *, message):
    await ctx.message.delete()
    await member.send(message)

@client.command()
async def announce(ctx, channel : discord.TextChannel, *, message):
    await ctx.message.delete()
    await channel.send(f"{message}")

@client.command()
async def dm_all(ctx, *, args=None):
    if args != None:
        members = ctx.guild.members
        for member in members:
            try:
                await member.send(args)
                print("'" + args + "' sent to: " + member.name)
 
            except:
                print("Couldn't send '" + args + "' to: " + member.name)
 
    else:
        await ctx.channel.send("A message was not provided.")

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="member-logs")
    if channel:
        embed = discord.Embed(
                description="Welcome to Yallabois F.C ",
                color=discord.Colour.red(),
            )
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_author(name=member.name, icon_url=member.avatar_url)
        embed.set_footer(text=member.guild, icon_url=member.guild.icon_url)
        embed.timestamp = datetime.datetime.utcnow()

        await channel.send(embed=embed)

@client.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name="member-logs")
    if channel:
        embed = discord.Embed(
                description="Goodbye from all of us.. ",
                color=discord.Colour.red(),
            )
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_author(name=member.name, icon_url=member.avatar_url)
        embed.set_footer(text=member.guild, icon_url=member.guild.icon_url)
        embed.timestamp = datetime.datetime.utcnow()

        await channel.send(embed=embed)
#poll command
@client.command()
async def poll(ctx,*args):
    embed = discord.Embed(title = f"POLLING\n{' '.join(args)}" , colour = discord.Colour.red())
    embed.description = f"YES: 🇾 \n\nNO : 🇳 "
    #embed.set_image(url = 'https://th.thgim.com/migration_catalog/article11163206.ece/alternates/FREE_435/modi%20symbol')
    message = await ctx.send(embed = embed)
    await message.add_reaction(emoji = '🇾')
    await message.add_reaction(emoji = '🇳')
    

        

#to catch deleted msg
@client.event
async def on_message_delete(message):
    client.sniped_messages[message.guild.id] = (message.content, message.author, message.channel.name, message.created_at)

@client.command()
async def snipe(ctx):
    try:
        contents, author, channel_name, time = client.sniped_messages[ctx.guild.id]
        
    except:
        await ctx.channel.send("Couldn't find a message to snipe!")
        return

    embed = discord.Embed(description=contents, color=discord.Color.purple(), timestamp=time)
    embed.set_author(name=f"{author.name}#{author.discriminator}", icon_url=author.avatar_url)
    embed.set_footer(text=f"Deleted in : #{channel_name}")

    await ctx.channel.send(embed=embed)


               
        
@client.command()
async def poda(ctx):
    if ctx.message.author.discriminator == '6012' :
        await ctx.send('Ok BOSS <a:polish_cow:767665553187012639>')
        await client.logout()
    else :
        await ctx.send('You messed With the Wrong Person')
'''client = Myclient()'''                                     
client.run("NzY2MjY0Njc1MzQ4MTE5NTUy.X4g1lw.NwjUbbIT9VtBeINDCe_uxX4CD0M")



