from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
load_dotenv()
from discord import Embed
from discord.ext import commands

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

intents = discord.Intents.all()
intents.members = True

app = commands.Bot(command_prefix='PREFIX',intents=intents)

@app.slash_command(name="botlist", description="Bot List") # 슬래시 커맨드 등록
async def mdlist(ctx: commands.Context): # 슬래시 커맨드 이름
    embed = Embed(title = "MDstudio Bot List",color=0x00AAFF)
    embed.set_footer(text="아로나 Arona : MD studio KR support bot")
    embed.set_footer(text="プラナ Plana : MD studio JP support bot")
    embed.set_footer(text="GSC : MD studio Global testing bot")
    await ctx.respond(embed=embed) # 인터렉션 응답

@app.event
async def on_ready():
    print('Done')
    await app.change_presence(status=discord.Status.online, activity=None)


try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
