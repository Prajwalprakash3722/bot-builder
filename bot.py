import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import datetime as dt
import random


# fucntions 

determine_who_goes_first(x, y):
    no = random.randint(1,2)
    if no == 1:
        return x
    else:
        return y




bot = commands.Bot(command_prefix="!")
# Things to run when the bot connects to Discord
@bot.event
async def on_ready():
    print("Connected!")


# Test command
@bot.command(pass_context=True)
async def new(ctx, p1: discord.Member, p2: discord.Member):
    await ctx.send(
        "Starting a new Game Between {} and {}".format(p1.mention, p2.mention)
    )
    user1 = p1
    user2 = p2
    first_player = determine_who_goes_first(user1, user2)
    if user1 and user2:
        await ctx.send(file=discord.File("sample.png"))
    else:
        await ctx.send("Please Select a player to play against!")
        await ctx.send("{} You go first!")


bot.run("ODYxODYzMTkwOTIxMDg0OTM5.YOP-pQ.qUj9883ylk8Vv0Inr9Xdkm_AdXw")
