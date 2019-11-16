import discord
from discord.ext import commands


class Useful(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases=['invite','invitecode','invcode'])
  async def inv(self, ctx):
      await ctx.send('https://discord.gg/eqtAFCa')

  @commands.command()
  async def info(self, ctx):
      await ctx.send('Made by <@!559903350024568833> for the SAFR community!')


def setup(client):
  client.add_cog(Useful(client))
  