BOT_PREFIX = "?"
BOT_TOKEN = ""
WELCOME_CHANNEL_ID = 806910868959920182 #Put it without " " Ex - 620498262436347905
LEAVE_CHANNEL_ID = 806979733539389450 #Put it without " " Ex - 620363449879052624

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = BOT_PREFIX, intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Logged in as "+bot.user.name)

@bot.event
async def on_member_join(member):
    await bot.wait_until_ready()
    try:
        channel = bot.get_channel(WELCOME_CHANNEL_ID)
        try:
            embed = discord.Embed(colour = discord.Colour.green())
            embed.set_author(name = member.name,icon_url = member.avatar_url)
            embed.add_field(name = "Welcome",value = f"**Hey,{member.mention}! Welcome to {member.guild.name}\nI hope you enjoy your stay here!\nThanks for joining**",inline = False)
            embed.set_thumbnail(url = member.guild.icon_url)
            await channel.send(embed = embed)
        except Exception as e:
            raise e
    except Exception as e:
        raise e

@bot.event
async def on_member_remove(member):
    await bot.wait_until_ready()
    try:
        channel = bot.get_channel(LEAVE_CHANNEL_ID)
        try:
            embed = discord.Embed(colour = discord.Colour.red())
            embed.set_author(name = member.name,icon_url = member.avatar_url)
            embed.add_field(name = "Good Bye",value = f"**{member.mention} just left us.**",inline = False)
            embed.set_thumbnail(url = member.guild.icon_url)
            await channel.send(embed = embed)
        except Exception as e:
            raise e
    except Exception as e:
        raise e

bot.run(BOT_TOKEN)

