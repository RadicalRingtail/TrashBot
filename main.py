import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import datetime
import pytz
import random
import os

#bot prefix and current time
bot = commands.Bot(command_prefix='/')
current_time = datetime.datetime.now(tz=pytz.UTC)
line_sep = '--------------------'

#sends message to console indicating that the bot has booted with out any errors
@bot.event
async def on_ready():
    print('Bot booted up at ' + str(current_time) + '\n' + line_sep)

#main info commands

#help command
@bot.command(pass_context=True)
async def helpme(ctx):
    await bot.say('**List of commands:**\n**/ping:** How to annoy a bot 101\n**/userinfor:** Gets info about a user\n**/serverinfo:** Gets info about the server you are currently in\n**/pfp:** Gets a users profile picture\n**/nuzzle:** Nuzzles you >w<\n**/groovycat:** Thats one hella groovy cat')
    print('executed help command' + '\n' + line_sep)

#ping command (work on getting the actual ping of bot connection)
@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say('dont ping me motherfucker')
    print('executed ping command' + '\n' + line_sep)

#user info command: gets data about user
@bot.command(pass_context=True)
async def userinfo(ctx, user: discord.Member):
    embed = discord.Embed(title='User info for {}'.format(user.name) + '#{}'.format(user.discriminator), description='Also known as: {}'.format(user.display_name))
    embed.set_thumbnail(url='{}'.format(user.avatar_url))
    embed.add_field(name='ID:', value='{}'.format(user.id))
    embed.add_field(name='Account created on:', value='{}'.format(user.created_at))
    embed.add_field(name='Joined on:', value='{}'.format(user.joined_at))
    embed.add_field(name='Current status:', value='{}'.format(user.status))
    embed.add_field(name='Currently playing:', value='{}'.format(user.game))
    await bot.say(embed=embed)
    print('executed info command' + '\n' + line_sep)

@userinfo.error
async def info_error(error, ctx):
    await bot.say('Please @ a user to view info about them!')
    print('returned error for info command (user arg not specified)' + '\n' + line_sep)

@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(title=ctx.message.server.name, description='Server region: {}'.format(ctx.message.server.region))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    embed.add_field(name="ID:", value=ctx.message.server.id)
    embed.add_field(name="Owner:", value=ctx.message.server.owner)
    embed.add_field(name="Server creation date:", value=ctx.message.server.created_at)
    embed.add_field(name="Members:", value=len(ctx.message.server.members))
    embed.add_field(name="Channels:", value=len(ctx.message.server.channels))
    embed.add_field(name="Roles:", value=len(ctx.message.server.roles))
    embed.add_field(name="Default role:", value=ctx.message.server.default_role)

    await bot.say(embed=embed)

@serverinfo.error
async def serverinfo_error(error, ctx):
    await bot.say("i just did a error, and basically, you're stupid")
    print(error + '\n' + line_sep)

#profile picture: gets users profile picture
@bot.command(pass_context=True)
async def pfp(ctx, user: discord.Member):
    embed = discord.Embed(title='{}'.format(user.name) + "'s profile picture: ")
    embed.set_image(url='{}'.format(user.avatar_url))
    await bot.say(embed=embed)
    print('executed pfp command' + '\n' + line_sep)

@pfp.error
async def pfp_error(error, ctx):
    await bot.say('Please @ a user to view their pfp!')
    print('returned error for pfp command (user arg not specified)' + '\n' + line_sep)

#fun commands

#nuzzle command: pings the user who uses the command and nuzzles them >w<
@bot.command(pass_context=True)
async def nuzzle(ctx):
    await bot.say('*nuzzles chu~* >w<')
    print('executed nuzzle command' + '\n' + line_sep)

@nuzzle.error
async def nuzzle_error(error, ctx):
    await bot.say('something went wrong when i tried to nuzzle you, oof')
    print('i literally just added this error catch just to be safe but if you actually somehow got this to show up in the console, i have no idea how you fucked this up')

#groovy cat command: posts a groovy cat
@bot.command(pass_context=True)
async def groovycat(ctx):
    await bot.send_file(ctx.message.channel, 'images/gifs/groovycat.gif')
    print('executed groovy cat command' + '\n' + line_sep)
    
#cursed image command: posts a random cursed image
@bot.command(pass_context=True)
async def cursedimage(ctx):
    await bot.send_file(ctx.message.channel, 'images/cursed images/' + random.choice(os.listdir('...\images\cursed images')))
    print('executed cursed image command' + '\n' + line_sep)



#search commands & web scraping

#soon

#bot key: dont share this plz kthx
bot.run('key')
