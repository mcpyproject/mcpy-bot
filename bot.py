import discord
import json
from discord.ext import commands

with open('config.json') as f:
    configData = json.load(f)

client = commands.Bot(command_prefix = configData['prefix'])

@client.event
async def on_ready():
    activity = discord.Game(name="PyCharm vs. Jupyter vs. Visual Studio Code", type=1)
    await client.change_presence(status=discord.Status.online, activity=activity)
    print('Bot is ready')

@client.command()
async def branch(ctx, arg):
    await ctx.send(f'You can access the {arg} branch by running ``git checkout {arg}``')

@client.command()
async def repo(ctx, arg):
    if (arg == 'main' or arg == 'mcpy'):
        await ctx.send('The github repo for McPy is located at https://github.com/mcpyproject/McPy')
    if (arg == 'bot'):
        await ctx.send('The github repo for the McPy discord bot is located at https://github.com/mcpyproject/mcpy-bot') 

@client.command()
async def tryitandsee(ctx):
    await ctx.send("It's now time to https://tryitands.ee")

@client.command()
async def install(ctx, arg):
    if (arg == 'python3' or arg == 'python3.8' or arg == 'python'):
        await ctx.send('Python 3.8 can be installed by following the instructions at https://www.python.org/downloads/release/python-387/')
    if (arg == 'submodules' or arg == 'submodule'):
        await ctx.send('In your McPy directory, run ``git submodule init`` and ``git submodule update``')
    if (arg == 'pip' or arg == 'pip3'):
        await ctx.send("Pip can be installed with either ``python3 -m ensurepip``, or on Debian-based Linux distributions use ``sudo apt install python3-pip``.")

client.run(configData['token'])