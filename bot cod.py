import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
@bot.event
async def on_message_edit(before, after):
    if before.content == after.content:
       return
    await before.channel.send("Сообщение было изменено!\n{before.content} -> {after.content}")

bot.run('ODM0NDU1MTQ2NjQ1NTUzMTgy.YIBI6g.y5hQXptSuKWfe1k6RlbwnKf5n0k')
