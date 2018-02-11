import discord
from discord.ext import commands
import datetime
import pytz
import random
import os

#bot prefix and current time
bot = commands.Bot(command_prefix='/')
current_time = datetime.datetime.now(tz=pytz.UTC)
line_sep = '--------------------'

#sends message to console indicating that the bot has booted with out any errors and also initializes some things
@bot.event
async def on_ready():
    print('Bot booted up at ' + str(current_time) + '\n' + line_sep)
    bot.remove_command('help')
    await bot.change_presence(game=discord.Game(name='Type "/helpme" for a list of commands'))

#main info commands

#help command
@bot.command(pass_context=True)
async def helpme(ctx):
    #have the string for this command load from a file cause this is way too long
    f = open('helpme.txt', 'r')
    await bot.say(f.read())
    f.close()
    print('executed help command' + '\n' + line_sep)

#ping command (work on getting the actual ping of bot connection)
@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say('dont ping me motherfucker')
    print('executed ping command' + '\n' + line_sep)

#user info command: gets data about a user
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

#server info command: gets data about the server the command is run in 
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

#github command: sends github page for TrashBot
@bot.command(pass_context=True)
async def github(ctx):
    await bot.say('TrashBot Github page: https://github.com/RadicalRingtail/TrashBot')

#fun commands

#nuzzle command: nuzzles you >w<
@bot.command(pass_context=True)
async def nuzzle(ctx):
    await bot.say('*nuzzles chu~* >w<')
    print('executed nuzzle command' + '\n' + line_sep)

@nuzzle.error
async def nuzzle_error(error, ctx):
    await bot.say('something went wrong when i tried to nuzzle you, oof')
    print('i literally just added this error catch just to be safe but if you actually somehow got this to show up in the console, i have no idea how you fucked this up' + '\n' + line_sep)

#groovy cat command: posts a groovy cat
@bot.command(pass_context=True)
async def groovycat(ctx):
    await bot.send_file(ctx.message.channel, 'images/gifs/groovycat.gif')
    print('executed groovy cat command' + '\n' + line_sep)

@groovycat.error
async def groovycat_error(error, ctx):
    await bot.say('the groovy cat is no where to be seen.')
    print('groovy cat command returned a error: image could not be found' + '\n' + line_sep)

#cursed image command: posts a random cursed image
@bot.command(pass_context=True)
async def cursedimage(ctx):
    await bot.send_file(ctx.message.channel, 'images/cursed images/' + random.choice(os.listdir('TrashBot\images\cursed images')))
    print('executed cursed image command' + '\n' + line_sep)

@cursedimage.error
async def groovycat_error(error, ctx):
    await bot.say('huh.. odd.. i could have sworn i had some cursed images here a second ago..')
    print('cursed image command returned a error: images or directory could not be found' + '\n' + line_sep)

#pong command
@bot.command(pass_context=True)
async def pong(ctx):
    await bot.say(':ping_pong:')

#search commands & web scraping

#soon

#bot key: dont share this plz kthx
bot.run('key')
