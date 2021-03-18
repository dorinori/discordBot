# bot.py

#things need to fix, error message when not pass through argument 
#when needed, help statements with description, require mention for punch
#statements, urban dictionary take in phrases too

import discord
import random
import os
import requests
import json
import glob
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

client = commands.Bot(command_prefix = '.')
# client.remove_command('help')

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    await client.change_presence(activity = discord.Activity(
                            type = discord.ActivityType.watching, 
                            name = 'The Untamed'))
# @client.event
# async def on_member_join(member):
#     print(f'{member} has joined a server.')

# @client.event
# async def on_member_remove(member):
#     print(f'{member} has left a server.')

@client.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Command not found.')

@client.command(help = "check your current ping")
async def ping(ctx):
    await ctx.send(f'Ping is {round(client.latency * 1000)} ms') 

@client.command(help = 'just try it ;)')
async def gif(ctx):
    response = requests.get('https://api.tenor.com/v1/search?q=肖战&key=' + os.environ['gif_key'] + '&limit=50')
    data = json.loads(response.text)
    gif_rand = random.randint(0, 50)
    gif_url = data['results'][gif_rand]['media'][0]['gif']['url']
    await ctx.send(gif_url)

@client.command(help = 'loser')
async def sean(ctx):
    response = requests.get('http://api.urbandictionary.com/v0/define?term=sean+wang')
    data = json.loads(response.text)
    definition = data['list'][0]['definition']
    example = data['list'][0]['example']
    link = data['list'][0]['permalink']
    parse = "[]"
    for char in parse:
        definition = definition.replace(char,'')
        example = example.replace(char,'')
    embed = discord.Embed(title = 'sean wang', color = discord.Colour.blue(), url = link)
    embed.add_field(name= "Definition", value= definition, inline = False)
    embed.add_field(name= "Example", value= example, inline = False)
    await ctx.send(embed = embed)

@client.command(help = 'xd')
async def ashley(ctx):
    response = requests.get('http://api.urbandictionary.com/v0/define?term=ashley+gong')
    data = json.loads(response.text)
    definition = data['list'][0]['definition']
    example = data['list'][0]['example']
    link = data['list'][0]['permalink']
    parse = "[]"
    for char in parse:
        definition = definition.replace(char,'')
        example = example.replace(char,'')
    embed = discord.Embed(title = 'ashley gong', color = discord.Colour.blue(), url = link)
    embed.add_field(name= "Definition", value= definition, inline = False)
    embed.add_field(name= "Example", value= example, inline = False)
    await ctx.send(embed = embed)

@client.command(help ='lol')
async def jesse(ctx):
    response = requests.get('http://api.urbandictionary.com/v0/define?term=jesse+ge')
    data = json.loads(response.text)
    definition = data['list'][0]['definition']   
    example = data['list'][0]['example'].replace('[', '')
    link = data['list'][0]['permalink']
    parse = "[]"
    for char in parse:
        definition = definition.replace(char,'')
        example = example.replace(char,'')
    embed = discord.Embed(title = 'jesse ge', color = discord.Colour.blue(), url = link)
    embed.add_field(name= "Definition", value= definition, inline = False)
    embed.add_field(name= "Example", value= example, inline = False)
    await ctx.send(embed = embed)

@client.command(aliases = ['urbandictionary'], help = "search any term ")
async def ud(ctx, *, arg):
    response = requests.get(f'http://api.urbandictionary.com/v0/define?term={arg}')
    data = json.loads(response.text)
    definition = data['list'][0]['definition']
    example = data['list'][0]['example']
    link = data['list'][0]['permalink']
    parse = "[]"
    for char in parse:
        definition = definition.replace(char,'')
        example = example.replace(char,'')
    embed = discord.Embed(title = arg, color = discord.Colour.blue(), url = link)
    embed.add_field(name = "Definition", value = definition, inline = False)
    embed.add_field(name = "Example", value = example, inline = False)
    await ctx.send(embed = embed)

@client.command(help='delete the last <amount> of messages')
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit = amount + 1)

@client.command(help = 'who would you like to punch?')
async def punch(ctx, person):
    rand_int = random.randint(0, 3)
    files = ['./punch/m_punch.gif', './punch/j_punch1.gif',
    './punch/moon_punch.gif']
    if (rand_int == 3):
        embed = discord.Embed(color = discord.Colour.blue(), 
        description = "Thats not nice! Here, have a smooch from Megan instead.")
        await ctx.send(file=discord.File('./punch/m_kiss.gif'))
        await ctx.send(embed = embed)
    else:
        embed = discord.Embed(color = discord.Colour.blue(), 
        description = f'{ctx.author.name} punched {person}')
        await ctx.send(file=discord.File(files[rand_int]))
        await ctx.send(embed = embed)

@client.command(help = 'try playing rock paper scissors with our bot')
async def rps(ctx, choice):
    hands = ['Rock', 'Paper', 'Scissors']
    outcome = random.choice(hands)
    if (choice.lower() == outcome.lower()):
        await ctx.send(f"{outcome}. Don't expect this to keep happening.")
    elif (choice.lower() == 'scissors'):
        if (outcome.lower() == 'rock'):
            await ctx.send(f"ROCK! Haha, you lose.")
        else:
            await ctx.send(f"Paper. Hmp, i'll beat you next time.")
    elif (choice.lower() == 'rock'):
        if (outcome.lower() == 'paper'):
            await ctx.send(f"Paper. You loser.")
        else:
            await ctx.send(f"Scissors, not cool.")
    elif (choice.lower() == 'paper'):
        if (outcome.lower() == 'rock'):
            await ctx.send(f"Rock. You're kind of bad at this game...")
        else:
            await ctx.send(f"Scissors. Darn, I can't believe I lost to *you*")

@client.command(aliases = ['8ball'], help= "ask me a question")
async def eightball(ctx, *, question):
    result = ["It is certain.",
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
        "Outlook not so good.",
        "Very doubtful."]
    await ctx.send(f'{random.choice(result)}')

@clear.error
async def clear_error(ctx,error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please specify an amount of message to delete.')

@ud.error
async def ud_error(ctx,error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please specify which word you want to search.')

@rps.error
async def rps_error(ctx,error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please specify which hand youre throwing: rock paper or scissors.')

@punch.error
async def punch_error(ctx,error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please specify who you want to punch.')

@eightball.error
async def eightball_error(ctx,error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please specify the question you want to ask.')

# @client.command(pass_context = True)
# async def help(ctx):
#     author = ctx.message.author
#     embed = discord.Embed(color = discord.Colour.orange())
#     embed.set_author(name = 'Help')
#     embed.add_field(name='.ashley, .jesse, .sean', value='For a special surprise ;)', inline = False)
#     embed.add_field(name='.ud [wordOrPhraseToLookUp] or .urbandictionary[wordOrPhraseToLookUp]', value='Search a term on urban dictionary', inline = False)
#     embed.add_field(name='.8ball [question]', value='Ask the 8ball a question!', inline = False)

#     await ctx.send(embed=embed)



client.run(os.getenv('TOKEN'))