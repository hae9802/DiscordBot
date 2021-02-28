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

token = os.environ['token']

# When the Bot RUN -> Status Change
@client.event
async def on_ready():
    print(client.user.name, 'has connected to Discord!')
    await client.change_presence(status=discord.Status.online, activity=discord.Game("업데이트"))
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
    embed.add_field(name="전적검색", value="사용 방법 : !전적 소환사이름", inline=False)
    embed.add_field(name="팀 분배", value="사용 방법 : !팀 이름,이름...,이름 (이름을 콤마로 이어주세요)", inline=False)

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


# !전적 -> ex) !전적 소환사이름
@client.command()
async def 전적(ctx, summonerName):
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

    for idx, i in enumerate(Sr):
        if idx == 0:
            embed = discord.Embed(title=Si['name'], color=0x00ffff)
            embed.add_field(name= "Level", value=str(Si['summonerLevel']), inline=False)
        else:
            embed = discord.Embed(title=None, color=0x00ffff)
        embed.add_field(name= str(i['queueType']),
            value=str(i['tier']) + ' ' + str(i['rank']) + ' ' + str(i['leaguePoints']) + str('LP'), inline=False)
        embed.add_field(name= "Win Rate",
            value=f"{i['wins'] + i['losses']}전 {i['wins']}승 {i['losses']}패 ({round(i['wins']/(i['wins'] + i['losses']) * 100, 2)}%) ", inline=False)
        embed.set_thumbnail(url=f"http://z.fow.kr/img/emblem/{i['tier'].lower()}.png")
        await ctx.send(embed=embed)



@client.command()
async def 팀(ctx, teams, name):
    tList = teams.split(',')
    nList = name.split(',')

    tlen = len(tList)
    nlen = len(nList)
    teamMax = nlen / tlen

    if nlen % tlen != 0:
        await ctx.send("입력을 확인해 주세요")
        return None
    
    embed = discord.Embed(title="팀 선정 결과", color=0xff00ff)
    tmpList = []

    count = 0
    for i in range(0, nlen):
        ind = random.randrange(0, nlen)
        tmpList.append(nList[ind])
        del nList[nList.index(nList[ind])]
        nlen = len(nList)
        if len(tmpList) == teamMax:
            embed.add_field(name=f"{tList[count]}", value=' '.join(tmpList), inline=False)
            count += 1
            tmpList.clear()
    
    await ctx.send(embed=embed)

    # endList1 = []
    # endList2 = []
    # if len(list) % 2 != 0:
    #     await ctx.send("인원이 맞지 않습니다")
    #     return None

    # for i in range(len(list)):
    #     if random.randrange(1,3) == 1 and len(endList1) < len(list) / 2:
    #         endList1.append(list[i])
    #     else:
    #         endList2.append(list[i])

    # embed = discord.Embed(title="팀 분배 결과", color=0x00ff00)
    # embed.add_field(name="1팀", value='\n'.join(endList1), inline=False)
    # embed.add_field(name="2팀", value='\n'.join(endList2), inline=False)
    # await ctx.send(embed=embed)



# # reaction added Event
# @client.event
# async def on_reaction_add(reaction, user):
#     if user.id == client.user.id:
#         return None
#     print(reaction.message.author.name)
#     print(reaction.emoji)
#     print(user.name)

# @client.event
# async def on_reaction_remove(reaction, user):
#     if(user.id == client.user.id):
#         return None
#     print(reaction.message.author.name)
#     print(reaction.emoji)
#     print(user.name)


# client Start
client.run(token)
