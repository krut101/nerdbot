import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix = '')

@bot.event
async def on_ready():
    print("Let's go! I'm ready!")
@bot.command(pass_context = True)
async def L(ctx):
    await bot.say("In process of handing the L to cookieXL...")
    await bot.say("Done!")
@bot.command(pass_context = True)
async def think(ctx):
    await bot.say(":thinking:")
@bot.command(pass_context = True)
async def bape(ctx):
    await bot.say("BAPE FTW")
bot.run("")
