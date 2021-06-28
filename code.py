
import discord
from discord.ext import commands
client = commands.Bot(command_prefix='!')
@client.command()
async def s(ctx):
   await ctx.send('hello')
@client.command()
async def hi(ctx):
   await ctx.send('hi')
client.run('ODU5MDcxMTQ1MjU3MDc0NzM4.YNnWWQ.loNGaOgJsrwSyzJRIYhOk6VHE4M')
