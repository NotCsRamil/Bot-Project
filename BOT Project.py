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
        "Command Executed BOSS "
        f"{member.mention} has been **kicked**")
    await member.kick(reason=reason)


@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await ctx.channel.send(
        "Ban Hammer Stuck "
        f"{member.mention} Cannot enter this **Server**")
    await member.ban(reason=reason)

@client.event
async def on_member_join(self, member):
        role = discord.utils.get(member.guild.roles, name='AMONG US')
        await member.add_roles(role)

@client.command()
async def shoot(ctx, amount=3):
    await ctx.channel.purge(limit=amount)

@client.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(client.latency*1000)}ms<a:cat_vibing:753973817608634468>')

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




        
    
        
           
               
        
@client.command()
async def poda(ctx):
    if ctx.message.author.discriminator == '6012' :
        await ctx.send('Ok BOSS <a:polish_cow:767665553187012639>')
        await client.logout()
    else :
        await ctx.send('You messed With the Wrong Person')
'''client = Myclient()'''                     
client.run("your bot token")



