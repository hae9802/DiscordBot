from logging import NOTSET
import discord
import asyncio
import random
from discord import embeds
from discord.ext.commands import bot
import datetime
import riot
import os


from discord.activity import Activity, CustomActivity
from discord.enums import ActivityType
from discord.ext import commands

client = commands.Bot(command_prefix='!')

# When the Bot RUN -> Status Change
@client.event
async def on_ready():
    print(client.user.name, 'has connected to Discord!')
    await client.change_presence(status=discord.Status.online, activity=discord.Game("!도움말"))
    print("[Bot : ready]")


# !배팅 -> ex) !배팅 주제 
@client.command()
async def 배팅(ctx, name):
    embed = discord.Embed(
        title="도박", description=name, color=0x00ffff)
    await ctx.send(embed=embed)
    embed = discord.Embed(title="선택", description="1 or 2", color=0xff00ff)
    embed.add_field(name=":one:", value="배당금", inline=False)
    embed.add_field(name=":two:", value="배당금", inline=True)
    message = await ctx.send(embed=embed)
    emojis = ["\U00000031\U0000FE0F\U000020E3",
              "\U00000032\U0000FE0F\U000020E3"]
    for emoji in emojis:
        await message.add_reaction(emoji)

# !주사위 -> Show Dice result
@client.command()
async def 주사위(ctx):
    r = random.randrange(1, 7)
    if r == 1:
        embed = discord.Embed(
            title="주사위 결과", description=":one:", color=0x0000ff)
    elif r == 2:
        embed = discord.Embed(
            title="주사위 결과", description=":two:", color=0x0000ff)
    elif r == 3:
        embed = discord.Embed(
            title="주사위 결과", description=":three:", color=0x0000ff)
    elif r == 4:
        embed = discord.Embed(
            title="주사위 결과", description=":four:", color=0x0000ff)
    elif r == 5:
        embed = discord.Embed(
            title="주사위 결과", description=":five:", color=0x0000ff)
    else:
        embed = discord.Embed(
            title="주사위 결과", description=":six:", color=0x0000ff)
    await ctx.send(embed=embed)


# !가위바위보 -> ex) !가위바위보 가위
@client.command()
async def 가위바위보(ctx, value):
    r = random.randrange(1, 3)
    if value == "가위":
        if r == 1:
            await ctx.send(":v:")
            embed = discord.Embed(
                title="가위바위보 결과", description="비겼습니다", color=0xff00ff)
        elif r == 2:
            await ctx.send(":fist:")
            embed = discord.Embed(
                title="가위바위보 결과", description="졌습니다", color=0xff00ff)
        else:
            await ctx.send(":raised_hand:")
            embed = discord.Embed(
                title="가위바위보 결과", description="이겼습니다", color=0xff00ff)
    elif value == "바위":
        if r == 1:
            await ctx.send(":v:")
            embed = discord.Embed(
                title="가위바위보 결과", description="이겼습니다", color=0xff00ff)
        elif r == 2:
            await ctx.send(":fist:")
            embed = discord.Embed(
                title="가위바위보 결과", description="비겼습니다", color=0xff00ff)
        else:
            await ctx.send(":raised_hand:")
            embed = discord.Embed(
                title="가위바위보 결과", description="졌습니다", color=0xff00ff)
    elif value == "보":
        if r == 1:
            await ctx.send(":v:")
            embed = discord.Embed(
                title="가위바위보 결과", description="졌습니다", color=0xff00ff)
        elif r == 2:
            await ctx.send(":fist:")
            embed = discord.Embed(
                title="가위바위보 결과", description="이겼습니다", color=0xff00ff)
        else:
            await ctx.send(":raised_hand:")
            embed = discord.Embed(
                title="가위바위보 결과", description="비겼습니다", color=0xff00ff)
    else:
        embed = discord.Embed(title="혹시 병신이십니까?", description="가위바위보에 대해서 잘 모르는 것 같군요!", color=0xff00ff)
        embed.add_field(name="가위바위보란?", value="https://han.gl/qB2Pl",inline=False)


    await ctx.send(embed=embed)

# !핑 -> Latency show
@client.command()
async def 핑(ctx):
    await ctx.trigger_typing()
    embed = discord.Embed(
        title="퐁!", description=f"{str(round(client.latency*1000))}ms", color=0x00ff00)
    embed.set_thumbnail(url=" https://han.gl/RYcbw")

    await ctx.send(embed=embed)


# !계산 -> ex) !계산 1 + 2
@client.command()
async def 계산(ctx, num1, op, num2):
    if op == "+":
        embed = discord.Embed(
            title="계산 결과", description=f"{str(int(num1) + int(num2))}", color=0x0000ff)
        embed.set_thumbnail(url=" https://han.gl/RYcbw")
        await ctx.send(embed=embed)
    elif op == "-":
        embed = discord.Embed(
            title="계산 결과", description=f"{str(int(num1) - int(num2))}", color=0x0000ff)
        embed.set_thumbnail(url=" https://han.gl/RYcbw")
        await ctx.send(embed=embed)

    elif op == "*":
        embed = discord.Embed(
            title="계산 결과", description=f"{str(int(num1) * int(num2))}", color=0x0000ff)
        embed.set_thumbnail(url=" https://han.gl/RYcbw")
        await ctx.send(embed=embed)
    elif op == "/":
        embed = discord.Embed(
            title="계산 결과", description=f"{str(int(num1) / int(num2))}", color=0x0000ff)
        embed.set_thumbnail(url=" https://han.gl/RYcbw")
        await ctx.send(embed=embed)


# !도움말 -> Author Dm
@client.command()
async def 도움말(ctx):
    message = await ctx.message.author.create_dm()
    embed = discord.Embed(title="사용 방법 및 명령어", color=0xff00ff)
    embed.add_field(name="!를 붙여주세요", value="Ex) !도움말", inline=True)
    embed.add_field(name="핑", value="사용 방법 : !핑", inline=False)
    embed.add_field(name="배팅", value="사용 방법 : !배팅 주제  (준비중...)", inline=False)
    embed.add_field(name="주사위", value="사용 방법 : !주사위", inline=False)
    embed.add_field(name="계산기", value="사용 방법 : !계산 숫자 수식 숫자", inline=False)
    embed.add_field(
        name="가위바위보", value="사용 방법 : !가위바위보 가위 or 바위 or 보", inline=False)
    embed.add_field(name="프로필확인", value="사용 방법 : !사진 @mention", inline=False)
    embed.add_field(name="전적검색 (솔랭)", value="사용 방법 : !솔랭 소환사이름", inline=False)

    embed.set_thumbnail(url=" https://han.gl/RYcbw")
    try:
        await ctx.send(f"{ctx.message.author.mention} DM을 확인해 주세요")
        await message.send(embed=embed)
    except:
        await ctx.send(f"{ctx.message.author.mention}님 서버 이름 클릭 - 개인정보 보호 설정 - 서버 멤버가 보내는 개인 메시지 허용해주세요.")


# for Develop Command
@client.command()
async def dev(ctx):
    print(client.user)
    print(ctx.message.channel.last_message.author)


# !사진 -> ex) !사진 @mention
@client.command()
async def 사진(ctx, user: discord.User):
    embed = discord.Embed(title=user.name+' 의 사진', color=0x0000ff)
    embed.set_image(url=user.avatar_url)
    await ctx.send(embed=embed)


# !솔랭 -> ex) !솔랭 소환사이름
@client.command()
async def 솔랭(ctx, summonerName):
    Si = riot.get_SummonerId(summonerName)
    if Si == 404:
        embed = discord.Embed(title="Unknown!", description="소환사 정보가 없습니다", color=0x00ffff)
        await ctx.send(embed=embed)
        return None
    elif Si == 403:
        embed = discord.Embed(title="API KEY GENERATE", description="API KEY 갱신이 필요합니다", color=0x00ffff)
        await ctx.send(embed=embed)
        return None


    Sr = riot.get_summonerRank(Si['id'])
    if not Sr:
        embed = discord.Embed(title=Si['name'], color=0x00ffff)
        embed.add_field(name= "UNRANKED", value="아직 배치를 완료하지 않았습니다", inline=False)
        await ctx.send(embed=embed)
        return None
    
    Sr = Sr[0]
    embed = discord.Embed(title=Si['name'], color=0x00ffff)
    embed.add_field(name= "Level", value=str(Si['summonerLevel']), inline=False)
    embed.add_field(name= "Solo Rank Tier",
        value=str(Sr['tier']) + ' ' + str(Sr['rank']) + ' ' + str(Sr['leaguePoints']) + str('LP'), inline=False)
    embed.add_field(name= "Win Rate",
        value=f"{Sr['wins'] + Sr['losses']}전 {Sr['wins']}승 {Sr['losses']}패 ({round(Sr['wins']/(Sr['wins'] + Sr['losses']) * 100, 2)}%) ", inline=False)

    await ctx.send(embed=embed)



# reaction added Event
@client.event
async def on_reaction_add(reaction, user):
    if user.id == client.user.id:
        return None
    print(reaction.message.author.name)
    print(reaction.emoji)
    print(user.name)

@client.event
async def on_reaction_remove(reaction, user):
    if(user.id == client.user.id):
        return None
    print(reaction.message.author.name)
    print(reaction.emoji)
    print(user.name)


# client Start
client.run(os.environ['token'])
