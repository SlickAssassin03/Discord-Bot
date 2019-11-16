import discord
from discord.ext import commands


class Utilities(commands.Cog):

  def __init__(self, client):
    self.client = client

  def is_Owner(ctx):
    return ctx.author.id == 559903350024568833

  @commands.command(aliases=['clearchat','purge'])
  @commands.has_permissions(manage_messages=True)
  @commands.check(is_Owner)
  async def clear(self, ctx, amount : int):
      await ctx.channel.purge(limit=amount)
  
  @commands.command(aliases=['p','latency'])
  @commands.check(is_Owner)
  async def ping(self, ctx):
      await ctx.send(f'Bot latency: {round(self.client.latency * 1000)}ms ')

  

def setup(client):
  client.add_cog(Utilities(client))
