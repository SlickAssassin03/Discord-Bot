import discord
import os
from serverutil import server
from util import console
from discord.ext import commands, tasks

token = os.environ.get('token')
client = commands.Bot(command_prefix = '/')
debug = 1

@client.event
async def on_ready():
    doPing.start()
    await client.change_presence(activity=discord.Game('First Response'))
    console.out(f'Logged in as {client.user}\nServer latency: {round((client.latency)*1000)}ms\nOnline and ready!')

#                   Reload
# ================================================

@client.command()
async def reload(ctx):
  if (debug==1):
    console.out('Reload starting!')
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game('Reloading...'))
    for filename in os.listdir('./cogs'):
      if filename.endswith('.py'):
        client.unload_extension(f'cogs.{filename[:-3]}')
    
    for filename in os.listdir('./cogs'):
      if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
    console.out('Reload complete!')
    await client.change_presence(status=discord.Status.online, activity=discord.Game('First Response'))
    await ctx.send('Reload complete!')

#                  Tasks
# ================================================

@tasks.loop(minutes=30)
async def doPing():
    console.out(f'Latency: {round((client.latency)*1000)}ms', 'Ping')


#                 Bot Start
# ================================================

server.life()

for filename in os.listdir('./cogs'):
      if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        console.out(f'Loaded package: cogs.{filename[:-3]}')

client.run(token)
