# bot.py
import discord
import random
import os
import requests
import json
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

# @client.command()
# async def ping(ctx):
#     await ctx.send(f'Ping is {round(client.latency * 1000)} ms') 

@client.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Command not found.')

@client.command(description='This is the full description')
async def gif(ctx):
    response = requests.get('https://api.tenor.com/v1/search?q=肖战&key=' + os.environ['gif_key'] + '&limit=50')
    data = json.loads(response.text)
    gif_rand = random.randint(0, 50)
    gif_url = data['results'][gif_rand]['media'][0]['gif']['url']
    await ctx.send(gif_url)

@client.command(description='This is the full description')
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

@client.command(description='This is the full description')
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

@client.command(description='This is the full description')
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

@client.command(Aliases = ['urbandictionary'], description='This is the full description')
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

@client.command(description='This is the full description')
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit = amount + 1)

@client.command(aliases = ['8ball'], description='This is the full description')
async def _8ball(ctx, *, question):
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