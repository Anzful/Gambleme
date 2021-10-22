import discord
from discord.ext import commands
import random
from keep_alive import keep_alive 

Token = 'My Token'

bot = commands.Bot(command_prefix = ',')

slot = [":seven:", ":apple:", ":pear:", ":grapes:", ":lemon:", ":strawberry:", ":peach:", ":coconut:", ":watermelon:"]
slot1 = [":seven:", ":apple:", ":pear:", ":grapes:", ":lemon:", ":strawberry:", ":peach:", ":coconut:", ":watermelon:"]
slot2 = [":apple:", ":pear:", ":grapes:", ":lemon:", ":strawberry:", ":peach:", ":coconut:", ":watermelon:"]
slot3 = [":seven:", ":apple:", ":pear:", ":grapes:", ":lemon:", ":strawberry:", ":peach:", ":coconut:", ":watermelon:"]


@bot.command()
async def play(ctx):
  embed = discord.Embed(title=random.choice(slot) +"  "+ random.choice(slot) +"  "+ random.choice(slot) + "\n" + "||"+  random.choice(slot1) +"  "+ random.choice(slot2) + "  "+  random.choice(slot3) + "||"+ "\n" +random.choice(slot) +"  "+ random.choice(slot) +"  "+ random.choice(slot),

  colour=discord.Colour.dark_gold())

  await ctx.send(embed=embed)


@bot.command()
async def hi(ctx):
  await ctx.send("hi")

@bot.event
async def on_ready():
    print('Hi!')
    await bot.change_presence(activity=discord.Game('Pillowphobic ⚰️'))


keep_alive()
bot.run(Token)
