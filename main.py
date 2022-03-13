import os
from asyncio import events
from os import name
import nextcord
from nextcord import activity
from nextcord import embeds
import asyncio
import json


from nextcord.embeds import Embed
from nextcord.ext.commands.core import check
from nextcord.shard import EventType
from nextcord.utils import get
from random import *
from math import *
from datetime import *
from nextcord import channel
from time import *
from nextcord.ext import commands,tasks,activities
from nextcord.http import Route
import youtube_dl
from youtube_dl import *

from nextcord import *
import datetime
from bs4 import BeautifulSoup
import requests
from PingPongTool import PingPong
import humanfriendly

yt_api_key = "AIzaSyA21HLcAEjVooEfUQNLaAOf5jXdR_1r7UY"
yt_api_key_m = "AIzaSyCm9gKtQc9IJlvx5pCNc_X5SwPtADiMCMM"

#==================================================================

ran = 0
back = 0
scratcher = 577266050769485844
noob = 711769839022243910
junjacger = 829200004136173618
liting = 796295126607593492
cookie = 892701268798218321
siba = 782841803530567680
madle = 849777888231555123
five = 871348411356545057

INTENTS = Intents.all()
p = "5"
client = commands.Bot(command_prefix = p,intents=INTENTS)

def random_color():
    return randint(0x000000,0xffffff)

def musicPlay(url , voice , option):
    voice.play(FFmpegPCMAudio(url, option) , lambda e : musicPlay(url , voice , option))

@tasks.loop()
async def change_bot():
    await client.change_presence(activity=Streaming(name=" | 서버수:{} | 핑:{}ms | ".format(len(client.guilds),int(client.latency * 1000)), url='https://www.youtube.com/watch?v=dWwRF4uewO8'))
    await asyncio.sleep(5)
    await client.change_presence(activity=Streaming(name=f" | {p}명령어 | ", url='https://www.youtube.com/watch?v=dWwRF4uewO8'))
    await asyncio.sleep(5)

uptime_s = 0
uptime_m = 0
uptime_h = 0
uptime_d = 0

@tasks.loop(seconds=1)
async def uptime():
    global uptime_s
    global uptime_m
    global uptime_h
    global uptime_d

    uptime_s +=1
    if uptime_s >= 60:
        uptime_s = 0
        uptime_m +=1
    if uptime_m >= 60:
        uptime_m = 0
        uptime_h += 1
    if uptime_h >= 24:
        uptime_h = 0
        uptime_d += 1
    

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('verson:2.0')
    print('------')
    change_bot.start()
    uptime.start()

#     ch = client.get_channel(949223351426105354)
#     embed = Embed(title = "규칙" , description = ">>> 1. 홍보를 금지\n\n2. 위급하지 않을경우 `@멘션` 금지\n\n3. 질문은 `개발 카테고리`에서 하세요" , color = 0xb000ff)
#     embed.set_footer(text = "이기능은 이봇에 존제하지않습니다.")
#     await ch.send(embed = embed , view = urlButton())

@client.slash_command(description = "봇의 핑을 보여줍니다")
async def 핑(inter : Interaction):
    ping = int(round(client.latency * 1000))
    embed = Embed(title = "퐁!", description = ("핑 : {}ms").format(ping),color = random_color())
    if ping <= 200 and ping > 100:
        embed.add_field(name = "보통 :yellow_square:", value = "by - {}".format(inter.user.name))
    elif ping <= 100:
        embed.add_field(name = "정상 :green_square:" ,value = "by - {}".format(inter.user.name))
    elif ping > 200:
        embed.add_field(name = "비정상 :red_square:" ,value = "by - {}".format(inter.user.name))
    await inter.response.send_message(embed = embed)

@client.slash_command(description = "채널을 만듬")
async def 채널만들기(inter : Interaction , 채널이름 : str = SlashOption(description = "채널이름")):
    if inter.user.guild_permissions.manage_channels:
        채널이름 = str(채널이름)
        채널이름 = 채널이름.replace("/","⁄").replace("#","⧣")
        await inter.guild.create_text_channel(name = 채널이름)
        await inter.response.send_message(f">>> {채널이름}채널을 만들었어요!")
    else:
        await inter.response.send_message(embed = Embed(title="당신은 권한이 없어요" , description=">>> 필요한 권한 : 채널관리") , ephemeral=True)
        return

@client.slash_command(description = "임베드를 만들수 있음")
async def 임베드만들기(inter: Interaction , 제목 : str = SlashOption(description="제목을 만듭니다") , 생성일  : str = SlashOption(description="생성일을 표시합니다 참일경우",choices = ["참","거짓"]) , 설명 : str = SlashOption(required = False , description = "설명") , 작은설명 : str = SlashOption(required = False , description = "작은설명") , 색상 : str = SlashOption(required = False , description = "색상")):
    try:
        if "0x" in 색상:color = eval(색상)
        else:color = eval(f"0x{색상}")
    except:color = 0x454545

    try:description = 설명.replace("\\n","\n")
    except:description = "​"

    try:footer = 작은설명
    except:footer = None

    if 생성일 == "참":timestamp = utils.utcnow()
    else:timestamp = ""
        

    embed = Embed(title = 제목.replace("\\n","\n") , description = description ,color = color , timestamp=timestamp)
    if footer != None:embed.set_footer(text = footer)

    await inter.response.send_message(embed = embed)

@client.slash_command(description = "로블록스 유저의 정보를 가저옵니다")
async def 로블록스(inter : Interaction , 로블록스이름 : str = SlashOption(description = "로블록스이름")):
    name = 로블록스이름

    id = requests.get(f"https://api.roblox.com/users/get-by-username?username={name}").json()["Id"]

    user_favorite_game = requests.get(f"https://games.roblox.com/v2/users/{id}/favorite/games?accessFilter=All&sortOrder=Asc&limit=50").json()
    user_game = requests.get(f"https://games.roblox.com/v2/users/{id}/games?sortOrder=Asc&limit=50").json()
    user = requests.get(f"https://users.roblox.com/v1/users/{id}").json()

    description = user["description"]
    create = f'{str(user["created"])[:4]}년{str(user["created"])[5:7]}월{str(user["created"])[8:10]}일'
    name = user["name"]
    display_name = user["displayName"]
    embed = Embed(title = f"{name}의 정보" , color = random_color())
    embed.add_field(name = "설명" , value=description+"᲻" , inline = False)
    embed.add_field(name = "표시닉" , value=display_name+"᲻" , inline = False)
    embed.add_field(name = "생성일" , value=create , inline = False)
    msg_name = ""
    try:
        for i in range(100):
            try:
                # game_description = user_game["data"][i]["description"]
                game_id = user_game["data"][i]["rootPlace"]["id"]
                game_name = str(user_game["data"][i]["name"]).replace(" ","-")
                game_link = f"https://www.roblox.com/games/{game_id}/{game_name}"
                msg_name += f"[{game_name.replace('-',' ')}]({game_link})\n"
            except:
                break
        embed.add_field(name = "자신의 게임" , value = msg_name+"᲻" , inline = False)

        msg_name = ""
        for i in range(100):
            try:
                # game_description = user_favorite_game["data"][i]["description"]
                game_id = user_favorite_game["data"][i]["rootPlace"]["id"]
                game_name = str(user_favorite_game["data"][i]["name"]).replace(" ","-")
                game_link = f"https://www.roblox.com/games/{game_id}/{game_name}"
                msg_name += f"[{game_name.replace('-',' ')}]({game_link})\n"
            except:
                break
        embed.add_field(name = "즐겨찾기를한 게임" , value = msg_name+"᲻" , inline = False)
        await inter.response.send_message(embed = embed)
    except:
        embed = Embed(title = f"{name}의 정보" , color = random_color())
        embed.add_field(name = "설명" , value=description+"᲻" , inline = False)
        embed.add_field(name = "표시닉" , value=display_name+"᲻" , inline = False)
        embed.add_field(name = "생성일" , value=create , inline = False)
        user_favorite_game = requests.get(f"https://games.roblox.com/v2/users/{id}/favorite/games?accessFilter=All&sortOrder=Asc&limit=50").json()
        user_game = requests.get(f"https://games.roblox.com/v2/users/{id}/games?sortOrder=Asc&limit=50").json()
        msg_name = ""
        for i in range(25):
            try:
                # game_description = user_game["data"][i]["description"]
                game_id = user_game["data"][i]["rootPlace"]["id"]
                game_name = str(user_game["data"][i]["name"]).replace(" ","-")
                game_link = f"https://www.roblox.com/games/{game_id}/{game_name}"
                msg_name += f"{game_name.replace('-',' ')}\n"
            except:
                break
        embed.add_field(name = "자신의 게임" , value = msg_name+"᲻" , inline = False)

        msg_name = ""
        for i in range(25):
            try:
                # game_description = user_favorite_game["data"][i]["description"]
                game_id = user_favorite_game["data"][i]["rootPlace"]["id"]
                game_name = str(user_favorite_game["data"][i]["name"]).replace(" ","-")
                game_link = f"https://www.roblox.com/games/{game_id}/{game_name}"
                msg_name += f"{game_name.replace('-',' ')}\n"
            except:
                break
        embed.add_field(name = "즐겨찾기를한 게임" , value = msg_name+"..." , inline = False)
        await inter.response.send_message(embed = embed)


@client.slash_command(description = "멤버를 타임아웃(뮤트) 시킴니다.")
async def 타임아웃(inter : Interaction , 멤버 : Member = SlashOption(description = "멤버") , 시간 : str = SlashOption(description = "시간") , 사유 : str = SlashOption(description = "사유")):
    try:
        if inter.user.guild_permissions.administrator or inter.user.id == scratcher:
            try:
                int(시간)
                시간 = str(시간)+"초"
            except:
                pass
            기간 = str(시간).replace("초","s").replace("분","m").replace("시간","h").replace("일","d").replace("주일","w").replace("주","w").replace("년","y")
            time = humanfriendly.parse_timespan(기간)
            print(time)

            max_time = 2419200.0
            if time > max_time:
                time = max_time
                시간 = "28일"
            
            await 멤버.edit(timeout=utils.utcnow() + datetime.timedelta(seconds=time))
            await inter.response.send_message(멤버.mention , embed = Embed(title = "타임아웃!",description = f"{멤버.mention} 님은 ``{시간}``동안 서버이용이 불가능합니다 \n\n사유:\n```\n{사유}\n```" , color= random_color()))
        else:
            await inter.response.send_message(embed = Embed(title="당신은 권한이 없어요" , description=">>> 필요한 권한 : 어드민") , ephemeral=True)
    except:
        await inter.response.send_message(embed = Embed(title="봇에게 권한이 없어요" , description=">>> 필요한 권한 : 어드민") , ephemeral=True)

@client.slash_command(description="개발자만 사용가능" , guild_ids = [899900037700669481])
async def 메세지보내기(inter : Interaction , id : str = SlashOption(description = "아이디") , message : str = SlashOption(description = "메세지")):
    if int(inter.channel_id) == 923831470219493376:
        member = utils.get(client.get_all_members(),id = int(id))
        try:
            await member.send(embed = Embed(title = "개발자에게서 메세지가 왔어요!" , description= f">>> {message}" , color = random_color() ))
            await inter.response.send_message(f"```ini\n[메세지보내기 성공] {message}```")
        except:
            await inter.send("```메세지를 보네지 못했어요!```")
    else:
        await inter.response.send_message(">>> 개발자만 사용할수 있어요!" , ephemeral = True)


@client.slash_command(description = "랜덤으로 이모지를 보냅니다.")
async def 이모지(inter : Interaction):
    def emojiLoop():
        global emojis
        try:
            guilds = client.guilds[randint(0,len(client.guilds)-1)]
            emojis = guilds.emojis[randint(0,len(guilds.emojis)-1)]
        except:
            emojiLoop()
    emojiLoop()
    if "a" in str(str(emojis).split("<")[1].split(":")[0]):
        emoji = (str(emojis).split(":")[2]).replace(">","")
        emoji_link = f"https://cdn.discordapp.com/emojis/{emoji}.gif?size=160"
    else:
        emoji = (str(emojis).split(":")[2]).replace(">","")
        emoji_link = f"https://cdn.discordapp.com/emojis/{emoji}.png?size=160"
    await inter.response.send_message(embed = Embed(title = f"이모지! {emojis}" , color = random_color()).set_image(url =  emoji_link) , view = DownEmoji(user = inter.user , url = emoji_link , name = str(emojis).replace("<","").replace(">","").split(":")[1]))

@client.slash_command(description = "투표")
async def 투표(inter : Interaction , 투표제목 : str = SlashOption(description = "투표의 제목을 써주세요") , 색상 : str = SlashOption(required = False , description = "색상")):
    if (색상 == None):
        color = random_color()
    else:
        색상 = 색상.replace("0x" , "")
        색상 = 색상.replace("#" , "")
        color = eval(f"0x{색상}")
    embed = Embed(title = 투표제목 , description = f"<:good:905078721881452565> | 0\n<:nooo:905078780421369946> | 0" , color = color)
    await inter.response.send_message(embed = embed , view = vote1(title = 투표제목))

@client.event
async def on_message(message):
    #준비시작------------------------------------------------

    if message.content.startswith(f"{p}상태"):
        await message.channel.send("""🟢│기본명령어 사용가능""")
    
    if message.content.startswith("//"):
        msg = str(message.content).replace("//","") 
        URL = "https://builder.pingpong.us/api/builder/61ab1bade4b0438b885d8379/integration/v0.2/custom/"
        Authorization = "Basic a2V5OmI1NzUyYjNlY2VlZGE4YzIyMWU1YTU5YjljM2UwZTUz"

        Ping = PingPong(URL, Authorization)

        data = dict(await Ping.Pong("Example", msg))["text"]
        await message.reply(data)

    #게임준비---------------------------------------------------------------
    if message.author.bot == False: 
        try:
            f = open("lvl.txt","r+")
            lvl_read = f.read()
            if str(message.author.id) in str(lvl_read):
                f.close()
                f = open("lvl.txt","w")
                lvl_exp = int(lvl_read.split(str(message.author.id))[1].split(":")[1])
                lvl = int(lvl_read.split(str(message.author.id))[1].split(":")[2])
                self_coin = int(lvl_read.split(str(message.author.id))[1].split(":")[3])
                tag = lvl_read.split(str(message.author.id))[1].split(":")[4]
                lvl_txt = lvl_read.replace("\n"+str((str(message.author.id)+f":{lvl_exp}:{lvl}:{self_coin}:{tag}:")),"")
                
                if tag == "1":
                    if randint(1,2) == 2:
                        lvl_exp += 1
                        print(1)
                if tag == "2":
                    if randint(1,2) == 2:
                        self_coin += 1
                        print(1)
                if tag == "3":
                    self_coin += 1
                    print(1)
                
                f.write("{}{}:{}:{}:{}:{}:\n".format(lvl_txt,message.author.id,int(lvl_exp)+1,lvl,self_coin,tag))
                f.close()
                f = open("lvl.txt","r")
                if lvl_exp+1 >= lvl**4:
                    lvl_exp = int(lvl_read.split(str(message.author.id))[1].split(":")[1])
                    lvl = int(lvl_read.split(str(message.author.id))[1].split(":")[2])
                    self_coin = int(lvl_read.split(str(message.author.id))[1].split(":")[3])
                    tag = lvl_read.split(str(message.author.id))[1].split(":")[4]
                    lvl_txt = lvl_read.replace("\n"+str((str(message.author.id)+f":{lvl_exp}:{lvl}:{self_coin}:{tag}:")),"")
                    lvl_exp = 0
                    lvl = int(lvl_read.split(str(message.author.id))[1].split(":")[2])
                    f.close()
                    f = open("lvl.txt","w")
                    f.write("{}{}:{}:{}:{}:{}:\n".format(lvl_txt,message.author.id,int(lvl_exp)+1,lvl+1,self_coin,tag))
                    f.close()
            else:
                if message.content.startswith(f"{p}참가"):
                    f.close()
                    f = open("lvl.txt","w")
                    f.write("{}{}:1:1:100:0:\n".format(lvl_read,message.author.id))
                    f.close()
                    await message.channel.send(embed = Embed(title = "완료!",description = "이제 게임 명령어를 사용할수 있어요",color= 0x00ff00))
                else:
                    pass
        except:
            try:
                f.write("{}{}:{}:{}:{}:{}:\n".format(lvl_txt,message.author.id,int(lvl_exp)+1,lvl+1,self_coin,tag))
                f.close()
            except:
                pass
    #준비끝------------------------------------------------
    global ran
    global back

    if message.content.startswith(f"{p}투표"):
        await message.delete()
        vote = message.content[4:].split("/")
        for i in range(2,len(vote)):
            embed = Embed(title ="투표:{}({})".format(vote[1],i-1),color = 0x00ff00,description = "{}".format(vote[i]))
            embed.set_footer(text = "by - {}".format(message.author.name))
            text= await message.channel.send(embed=embed)
            await text.add_reaction('<:good:905078721881452565>')
            await text.add_reaction('<:nooo:905078780421369946>')

    if message.content.startswith(f"{p}청소"):
        if message.author.id == scratcher or message.author.guild_permissions.manage_messages:
            num = message.content.split(" ")[1]
            if num == "모두":
                num = 9999999999999999999999999999999999999999999999
                int(num)
                await message.delete()
                await message.channel.purge(limit = num)
                embed = Embed(title ="모든메세지가 삭제 되었습니다",color = 0x000fff)
                embed.set_footer(text = "by - {}".format(message.author.name))
                await message.channel.send(embed=embed)
            else:
                num = int(num)
                if num >= 9999999999999999999999999999999999999999999999:
                    num = 9999999999999999999999999999999999999999999999
                await message.delete()
                await message.channel.purge(limit = num)
                embed = Embed(description ="메세지{}개가 삭제 되었습니다".format(num),color = 0x000fff)
                embed.set_footer(text = "by - {}".format(message.author.name))
                await message.channel.send(embed=embed)
        else:
            embed = Embed(description ="{}님은 5청소를 사용할권한이 없습니다".format(message.author.mention),color = 0x000fff)
            await message.channel.send(embed=embed)
    if message.content.startswith(f"{p}clear") or message.content.startswith(f"{p}c"):
        if message.author.id == scratcher or message.author.guild_permissions.manage_messages:
            num = int(message.content.split(" ")[1])
            await message.delete()
            await message.channel.purge(limit = num)
        else:
            embed = Embed(description ="{}님은 5clear를 사용할권한이 없습니다".format(message.author.mention),color = 0x000fff)
            await message.channel.send(embed=embed)

    if message.content.startswith(f"{p}공지"):
        if message.author.id == scratcher or message.author.guild_permissions.manage_messages:
            await message.delete()
            text1 = message.content[4:].split("/")
            embed = Embed(title ="공지:{}".format(text1[1]),color = 0xff0000,description = text1[2])
            embed.set_footer(text = "by - {}".format(message.author.name))
            await message.channel.send(embed=embed)
        else:
            embed = Embed(title ="{}님은 5공지를 사용할권한이 없습니다".format(message.author.mention),color = 0x000fff)
            await message.channel.send(embed=embed)
    if message.content.startswith(f"{p}수학"):
        embed = Embed(title = "수학",
        description ="""
sin 각도
cos 각도
tan 각도
""",
        color = 0x00ff00)
        await message.channel.send(embed = embed)
    if message.content.startswith("sin"):
        s = message.content[4:]
        s = int(s)
        embed = Embed(title = "sin {} = {}".format(s , sin(s)) , color = 0xff0000)
        await message.channel.send(embed = embed)

    if message.content.startswith("cos"):
        co = message.content[4:]
        co = int(co)
        embed = Embed(title = "cos {} = {}".format(co , cos(co)) , color = 0xff0000)
        await message.channel.send(embed = embed)

    if message.content.startswith("tan"):
        t = message.content[4:]
        t = int(t)
        embed = Embed(title = "tan {} = {}".format(t , tan(t)) , color = 0xff0000)
        await message.channel.send(embed = embed)

    if message.content.startswith(f"{p}정보"):
        try: 
            user = message.mentions[0]
        except:
            user = message.author
        req = requests.get(f"https://koreanbots.dev/api/v2/users/{user.id}").json()
        bots = ""
        try:
            for bot in req['data']['bots']:
                bots = f"{bots}[{bot['name']}]({bot['url']})\n"
        except:
            pass
        if bots == "":
            bots = "없음"
        user_ = str(datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000))
        embed = Embed(title = f"__{user}__님의 정보")
        embed.add_field(name = "이름" , value = user.name,inline=True)
        embed.add_field(name = "별명" , value = user.display_name,inline=True)
        embed.add_field(name = "아이디" , value = user.id,inline=True)
        embed.add_field(name = "소유한 봇" , value = bots,inline=True)
        embed.add_field(name="가입일",value=f"{user_[:4]}년{user_[5:7]}월{user_[8:10]}일")
        embed.set_thumbnail(url = user.avatar)
        await message.channel.send(embed = embed)

    if message.content.startswith(f"{p}핑"):
        ping = int(round(client.latency * 1000))
        embed = Embed(title = "핑", description = ("핑 : {}ms").format(ping),color = random_color())
        if ping <= 200 and ping > 100:
            embed.add_field(name = "보통 :yellow_square:", value = "by - {}".format(message.author.name))
        elif ping <= 100:
            embed.add_field(name = "정상 :green_square:" ,value = "by - {}".format(message.author.name))
        elif ping > 200:
            embed.add_field(name = "비정상 :red_square:" ,value = "by - {}".format(message.author.name))
        await message.channel.send(embed = embed)
#윷놀이--------------------------------------------------
    if message.content.startswith("!봇"):
        if message.author.id == scratcher :
            await message.delete()
            text3 = message.content[3:]
            await message.channel.send(text3)

    if message.content.startswith(f'{p}답변') or message.content.startswith(f'{p}답장'):
        if message.author.id == scratcher or message.author.id == liting or message.author.id == junjacger or message.author.id == cookie or message.author.id ==siba or message.author.id == noob or message.author.id == madle or message.author.id == five:
            msg = message.content[4:].split("/")[1]
            await message.channel.send(f"```답변/답장 을 성공하였습니다\n내용:{msg}```")
            try:
                member = message.mentions[0]
                embed = Embed(title=f"{message.author.name}님이 당신께 답변을 보냈습니다", description=msg,timestamp=message.created_at, color = 0x5F00FF)
                await member.send(embed=embed)
            except:
                member = utils.get(client.get_all_members(),id = int(message.content[4:].split("/")[0]))
                embed = Embed(title=f"{message.author.name}님이 당신께 답변을 보냈습니다", description=msg,timestamp=message.created_at, color = 0x5F00FF)
                await member.send(embed=embed)
            await message.delete()
        else:
            await message.channel.send("관리자가 아닙니다")
    
    # if ("https://" in message.content or "http://" in message.content) and (("tenor.co" in message.content) == False and ("media.discordapp.net" in message.content) == False and ("https://cdn.discordapp.com/emojis/" in message.content) == False):
    #     f = open("svr.txt","r")
    #     if (str(message.guild.id) in str(f.read())) == False:
    #         await message.add_reaction('<:xx:905014703577772063>')
    #         f.close()
        
    if message.content.startswith(f"{p}슬로우"):
        if message.author.guild_permissions.administrator or message.author.id == scratcher:
            number = message.content.split(" ")[1]
            try:
                if number in "0":
                    await message.channel.edit(slowmode_delay=0)
                    embed1 = Embed(title=f"채널 슬로우 모드를 {number}초로 설정했습니다!",color=0xFF00DD)
                    await message.reply(embed=embed1)
                elif int(number) > 21600 or int(number) <= 0:
                    raise commands.BadArgument
                else:
                    await message.channel.edit(slowmode_delay=float(number))
                    embed1 = Embed(title=f"채널 슬로우 모드를 {number}초로 설정했습니다!",color=0xFF00DD)
                    await message.reply(embed=embed1)
            except:
                await message.reply(embed=Embed(title = "...",description = "정수와0만 사용할수있어요!"))
        else:
            embed2= Embed(title="명령어를 사용할 수 있는 권한이 없어요!", color=0xFF0000)
            await message.channel.send(embed=embed2)

    if message.content.startswith(f"{p}현재"):
        y = str(datetime.datetime.now())[:4]
        m = int(str(datetime.datetime.now())[11:13])
        y_1 = int(y[3:])
        y_2 = int(y)%12

        if y_1 == 4:
            t_1 = "갑"
        if y_1 == 5:
            t_1 = "을"
        if y_1 == 6:
            t_1 = "병"
        if y_1 == 7:
            t_1 = "정"
        if y_1 == 8:
            t_1 = "무"
        if y_1 == 9:
            t_1 = "기"
        if y_1 == 0:
            t_1 = "경"
        if y_1 == 1:
            t_1 = "신"
        if y_1 == 2:
            t_1 = "임"
        if y_1 == 3:
            t_1 = "계"

        if y_2 == 4:
            t_2 = "자"
        if y_2 == 5:
            t_2 = "축"
        if y_2 == 6:
            t_2 = "인"
        if y_2 == 7:
            t_2 = "묘"
        if y_2 == 8:
            t_2 = "진"
        if y_2 == 9:
            t_2 = "사"
        if y_2 == 10:
            t_2 = "오"
        if y_2 == 11:
            t_2 = "미"
        if y_2 == 0:
            t_2 = "신"
        if y_2 == 1:
            t_2 = "유"
        if y_2 == 2:
            t_2 = "술"
        if y_2 == 3:
            t_2 = "해"
        t_all = str(t_1+t_2+"년")

        if "갑" in t_all[:1]:
            t_all+="(甲"
        if "을" in t_all[:1]:
            t_all+="(乙"
        if "병" in t_all[:1]:
            t_all+="(丙"
        if "정" in t_all[:1]:
            t_all+="(丁"
        if "무" in t_all[:1]:
            t_all+="(戊"
        if "기" in t_all[:1]:
            t_all+="(己"
        if "경" in t_all[:1]:
            t_all+="(庚"
        if "신" in t_all[:1]:
            t_all+="(辛"
        if "임" in t_all[:1]:
            t_all+="(壬"
        if "계" in t_all[:1]:
            t_all+="(癸"

        if "자" in t_all[1:]:
            t_all+="子年)\n**--------띠--------**\n쥐띠"
        if "축" in t_all[1:]:
            t_all+="丑年)\n**--------띠--------**\n소띠"
        if "인" in t_all[1:]:
            t_all+="寅年)\n**--------띠--------**\n범띠(호랑이띠)"
        if "묘" in t_all[1:]:
            t_all+="卯年)\n**--------띠--------**\n토끼띠"
        if "진" in t_all[1:]:
            t_all+="辰年)\n**--------띠--------**\n용띠"
        if "사" in t_all[1:]:
            t_all+="巳年)\n**--------띠--------**\n뱀띠"
        if "오" in t_all[1:]:
            t_all+="午年)\n**--------띠--------**\n말띠"
        if "미" in t_all[1:]:
            t_all+="未年)\n**--------띠--------**\n양띠"
        if "신" in t_all[1:]:
            t_all+="申年)\n**--------띠--------**\n원숭이띠"
        if "유" in t_all[1:]:
            t_all+="酉年)\n**--------띠--------**\n닭띠"
        if "술" in t_all[1:]:
            t_all+="戌年)\n**--------띠--------**\n개띠(강아지띠)"
        if "해" in t_all[1:]:
            t_all+="亥年)\n**--------띠--------**\n돼지띠"

        if m >= 23 and m < 1:
            t_all+="\n**-------시간-------**\n자시(子時) : 쥐가 제일 열심히 뛰어 다니는 때"
        if m >= 1 and m < 3:
            t_all+="\n**-------시간-------**\n축시(丑時) : 밤새 풀을 먹은 소가 한참 반추하며 아침 밭갈이 준비를 할 때"
        if m >= 3 and m < 5:
            t_all+="\n**-------시간-------**\n인시(寅時) : 하루 중 호랑이가 제일 흉악한 때"
        if m >= 5 and m < 7:
            t_all+="\n**-------시간-------**\n묘시(卯時) : 해뜨기 직전에 달이 아직 중천에 걸려 있어 그 속에 옥토끼가 보이는때"
        if m >= 7 and m < 9:
            t_all+="\n**-------시간-------**\n진시(辰時) : 용들이 날면서 강우 준비를 하는 때"
        if m >= 9 and m < 11:
            t_all+="\n**-------시간-------**\n사시(巳時) : 이 시간에 뱀은 자고 있어 사람을 해치는 일이 없는 때"
        if m >= 11 and m < 13:
            t_all+="\n**-------시간-------**\n오시(午時) : 이 시간에는 고조에 달했던 ‘양기’가 점점 기세를 죽이며 ‘음기’ 가 머리를 들기 시작하는데, 말은 땅에서 달리고 땅은 ‘음기’이므로 말을 ‘음기’의 동물로 보고 이 시각을 말과 연계시킨다."
        if m >= 13 and m < 15:
            t_all+="\n**-------시간-------**\n미시(未時) : 양이 이때 풀을 뜯어먹어야 풀이 재생하는데 해가 없다"
        if m >= 15 and m < 17:
            t_all+="\n**-------시간-------**\n신시(申時) : 이 시간에 원숭이가 울음소리를 제일 많이 낸다."
        if m >= 17 and m < 19:
            t_all+="\n**-------시간-------**\n유시(酉時) : 하루 종일 모이를 쫓던 닭들이 둥지에 들어가는 때"
        if m >= 19 and m < 21:
            t_all+="\n-------시간-------\n술시(戌時) : 날이 어두워지니 개들이 집을 지키기 시작하는 때"
        if m >= 21 and m < 0 or m >= 21 and m < 24:
            t_all+="\n**-------시간-------**\n해시(亥時) : 이 시간에 돼지가 가장 단잠을 자고 있는 시간이다."
        t_all = "**-------년도-------**\n"+t_all
        await message.channel.send(embed = Embed(title = "지금은?",description= t_all,color = random_color()))
    
    if message.content.startswith(f"{p}타이머"):
        timer = await message.channel.send(embed = Embed(title=">>> {}님의 타이머__{}초__".format(message.author,message.content.split(" ")[1]),description=">>> {}".format(message.content.split(" ")[1]),color = random_color()))
        for i in range(int(timer.embeds[0].description[4:])):
            await asyncio.sleep(1)
            timer_time = int(timer.embeds[0].description[4:])
            timer_time -= 1
            timer = await timer.edit(embed = Embed(title=timer.embeds[0].title,description=">>> {}".format(timer_time),color = random_color()))
        timer = await timer.edit(embed = Embed(title=timer.embeds[0].title,description=">>> TIMEOVER!",color = 0xff0000))
    
    if message.content.startswith(f"{p}코로나"):
        e = await message.channel.send(embed = Embed(title="사이트를 불러오는중...",color = random_color()))
        req = requests.get("https://api.corona-19.kr/korea/?serviceKey=5vH8sL1K6PGxkbIMla4r3jnAEgRuZYFqi").json()
        req2 = requests.get("https://api.corona-19.kr/korea/country/new/?serviceKey=5vH8sL1K6PGxkbIMla4r3jnAEgRuZYFqi").json()

        await e.edit(embed = Embed(title="기준일을 불러오는중...",color = random_color()))
        기준 = "{}".format(req['updateTime'])
        await e.edit(embed = Embed(title="확진환자를 불러오는중...",color = random_color()))
        확진환자 = "{} + {}".format(req['TotalCase'] , req2['korea']["newCase"])
        await e.edit(embed = Embed(title="격리해제를 불러오는중...",color = random_color()))
        격리해제 = "{} + {}".format(req['TotalRecovered'] , req['TodayRecovered'])
        await e.edit(embed = Embed(title="치료중을 불러오는중...",color = random_color()))
        치료중 = "{} + {}".format(req['NowCase'] , req['TotalCaseBefore'])
        await e.edit(embed = Embed(title="사망을 불러오는중...",color = random_color()))
        사망 = "{} + {}".format(req['TotalDeath'] , req['TodayDeath'])
        await e.edit(embed = Embed(title="합성중...",color = random_color()))
        embed = Embed(title=f">>> 기준일 | {기준}",description=f">>> **확진환자 | {확진환자}\n격리해제 | {격리해제}\n치료중(격리중) | {치료중}\n사망 | {사망}**",color = random_color(),url="http://ncov.mohw.go.kr/")
        embed.set_thumbnail(url ="https://api.corona-19.kr/")
        await e.edit(embed = embed)
    
    if message.content.startswith(f"{p}만들기"):
        if message.content == f"{p}만들기" or message.content == f"{p}만들기 ":
            embed = Embed(title=f"{p}만들기 사용방법")
            embed.add_field(name = "기본규칙",value=">>> 1.메세자끝에는 세미콜론(**;**)이들어가야합니다\n2.명령어를 사용하려면 명령어뒤에 **띄어쓰기** 를해야합니다",inline=True)
            embed.add_field(name = "제목",value=">>> 제목은 뒤에값이 들어갑니다 말그대로 임베드의 제목입니다\nex)!만들기 제목 테스트;",inline=True)
            embed.add_field(name = "설명",value=">>> 설명은 제목과같이 뒤에값이 들어갑니다 하지만 제목보다 크기가작습니다\nex)!만들기 설명 테스트;",inline=True)
            embed.add_field(name = "색상",value=">>> 색상은 제목 또는 설명이 있어야 사용가능합니다 색상은 0x0000ff(0x|(R)00|(G)00|(B)ff|)로 나타냅니다\nex)!만들기 설명 테스트;색상 0x110033;",inline=True)
            embed.add_field(name = "사진",value=">>> 이미지는 이미지 + 사진 형식으로 사용할수 있습니다\nex)!만들기 이미지 ``사진``;",inline=True)
            embed.add_field(name = "이미지",value=">>> 사진은 사진 + 사진 형식으로 사용할수 있습니다\nex)!만들기 사진 ``사진``;",inline=True)
            embed.add_field(name = "만든날",value=">>> 만든날은 제목 또는 설명이 있어야 사용가능하며 뒤에 값이안들어갑니다\nex)!만들기 설명 테스트;만든날;",inline=True)
            embed.add_field(name = "답변/답장방지",value=">>> 답변을 방장을 방지합니다\nex)!만들기 설명 테스트;답변/답장방지;",inline=True)
            await message.channel.send(embed = embed)
        else:
            try:
                color = 0x454545
                description = ""
                title = ""
                timestamp = ""
                img1 = ""
                img2 = ""
                if "제목" in message.content:
                    title = message.content.split("제목 ")[1].split(";")[0]
                if "설명" in message.content:
                    description = message.content.split("설명 ")[1].split(";")[0]
                if "색상" in message.content:
                    color = str(message.content.split("색상 ")[1].split(";")[0])
                    try:
                        color = color.replace(" ","")
                    except:
                        pass
                    color = eval(color)
                if "만든날" in message.content:
                    timestamp = datetime.datetime.now()
                if "이미지" in message.content:
                    img1 = str(message.attachments[0])
                if "사진" in message.content:
                    img2 = str(message.attachments[0])
                if "답변방지" in message.content or "답장방지" in message.content:
                    a = 1
                else:
                    a = 0
                embed = Embed(title=title,description=description,color=color,timestamp=timestamp)
                embed.set_thumbnail(url=img1)
                embed.set_image(url=img2)
                if a == 0:
                    await message.reply(embed = embed)
                else:
                    await message.channel.send(embed = embed)
            except:
                await message.reply(embed = Embed(title="오류!",description="명령어를 제대로 사용해주세요",color = 0xff0000))

    if message.content.startswith(f"{p}유튜브"):
        try:
            txt = str(message.content).replace(f"{p}유튜브","")
            if str(txt[0]) == " ":
                txt = txt[1:]
            else:
                pass
            res = requests.get(f"https://youtube.googleapis.com/youtube/v3/search?q={txt}&part=snippet&type=channel&maxResults=50&key={yt_api_key}&alt=json",headers={'User-Agent': 'Mozilla/5.0'}).json()
            for item in sorted(res['items'] , key=lambda x:x['snippet']['publishedAt']):
                if txt in item['snippet']['title']:
                    nopeapi = 0
                    if str(message.author.name[:2]) in str(item['snippet']['title']):
                        title = item['snippet']['title']
                        link = "https://www.youtube.com/channel/{}".format(item['snippet']['channelId'])
                        description = item['snippet']['description'] + "ㅤ"
                        img = item['snippet']['thumbnails']['high']['url']
                        publishTime = item['snippet']['publishTime']
                        embed = Embed(title=f"유튜버 - {title}님의정보",color = random_color())
                        embed.set_thumbnail(url=img)
                        embed.add_field(name="설명",value=description)
                        embed.add_field(name="채널 개설일",value=publishTime)
                        link = link.replace("ㅤ","").replace(" ","")
                        embed.add_field(name="채널링크",value=f"[링크]({link})")
                        await message.reply(embed = embed)
                        nopeapi = 1
                        break
                    else:
                        nopeapi = 0
                else:
                    nopeapi = 0
            if nopeapi==0:
                res = requests.get(f"https://youtube.googleapis.com/youtube/v3/search?q={txt}&part=snippet&type=channel&key={yt_api_key}&alt=json",headers={'User-Agent': 'Mozilla/5.0'}).json()
                for item in sorted(res['items'] , key=lambda x:x['snippet']['publishedAt']):
                    if txt in item['snippet']['title']:
                        title = item['snippet']['title']
                        link = "https://www.youtube.com/channel/{}".format(item['snippet']['channelId'])
                        description = item['snippet']['description'] + "ㅤ"
                        img = item['snippet']['thumbnails']['high']['url']
                        publishTime = item['snippet']['publishTime']
                        embed = Embed(title=f"유튜버 - {title}님의정보",color = random_color())
                        embed.set_thumbnail(url=img)
                        embed.add_field(name="설명",value=description)
                        embed.add_field(name="채널 개설일",value=publishTime)
                        link = link.replace("ㅤ","").replace(" ","")
                        embed.add_field(name="채널링크",value=f"[링크]({link})")
                        await message.reply(embed = embed)
                        nopeapi2 = 1
                        break
                    else:
                        nopeapi2 = 0
                if nopeapi2 == 0:
                    for item in sorted(res['items'] , key=lambda x:x['snippet']['publishedAt']):
                        title = item['snippet']['title']
                        link = "https://www.youtube.com/channel/{}".format(item['snippet']['channelId'])
                        description = item['snippet']['description'] + "ㅤ"
                        img = item['snippet']['thumbnails']['high']['url']
                        publishTime = item['snippet']['publishTime']
                        embed = Embed(title=f"유튜버 - {title}님의정보",color = random_color())
                        embed.set_thumbnail(url=img)
                        embed.add_field(name="설명",value=description)
                        embed.add_field(name="채널 개설일",value=publishTime)
                        link = link.replace("ㅤ","").replace(" ","")
                        embed.add_field(name="채널링크",value=f"[링크]({link})")
                        await message.reply(embed = embed)
                        break
        except:
            await message.reply(embed = Embed(title="오류!",description="채널을 찾을수 없습니다",color=0xff0000))
    
    if message.content.startswith(f"{p}서버정보"):
        try:
            bot = 0
            for i in range(message.guild.member_count):
                if message.guild.members[i].bot:
                    bot += 1
            ran_col = random_color()
            embed = Embed(title=f'"{message.guild.name}"의 정보',color = ran_col)
            embed.set_thumbnail(url=message.guild.icon)
            embed.add_field(name="서버주인",value=str(message.guild.owner.mention)+"ㅤ")
            embed.add_field(name="인증단계",value=(str(message.guild.verification_level)+"ㅤ").replace("none","없음").replace("low","낮음").replace("medium","중간").replace("high","높음").replace("highest","매우 높음") )
            user_ = str(datetime.datetime.utcfromtimestamp(((int(message.guild.id) >> 22) + 1420070400000) / 1000))
            embed.add_field(name="생성일",value=f"{user_[:4]}년{user_[5:7]}월{user_[8:10]}일ㅤ")
            embed.add_field(name="멤버",value=f"{message.guild.member_count}명ㅤ")
            embed.add_field(name="봇",value=f"{bot}명ㅤ")
            embed.add_field(name="순멤버",value=f"{message.guild.member_count-bot}명ㅤ")
            a = await message.channel.send(embed = embed)
            all_emoji = ""
            for i in range(len(message.guild.emojis)):
                all_emoji += str(message.guild.emojis[i])+"ㅤ"
            try:
                await message.channel.send(embed = Embed(title = "이모지",description=all_emoji,color = ran_col))
            except:
                await message.channel.send(embed = Embed(title = "이모지가 너무많아서 숫자로 불렀어요!",description=len(message.guild.emojis)+"개",color = ran_col))
        except:
            await message.channel.send(embed = Embed(title="봇에 권한이 없어요",color = 0xff0000))
    
    if message.content.startswith(f"{p}킥"):
        if message.author.guild_permissions.kick_members or message.author.id == scratcher:
            user = message.mentions[0]
            msg = (message.content[25:])
            await message.delete()
            await user.send(embed = Embed(title=f"{message.author}님이 당신을 킥했습니다",description=f"사유:{msg}.",color = 0xff0000))
            await message.channel.send(embed = Embed(title=f"{message.author}님이 {user}을/를 킥했습니다",description=f"사유:{msg}",color = 0xff0000))
            await user.kick()
        else:
            await message.channel.send(embed = Embed(title="권한이 없어요",color=0xff0000))
    if message.content.startswith(f"{p}밴") or message.content.startswith(f"{p}벤"):
        if message.author.guild_permissions.ban_members or message.author.id == scratcher:
            user = message.mentions[0]
            msg = (message.content[25:])
            await message.delete()
            await user.send(embed = Embed(title=f"{message.author}님이 당신을 밴했습니다",description=f"사유:{msg}",color = 0xff0000))
            await message.channel.send(embed = Embed(title=f"{message.author}님이 {user}을/를 밴했습니다",description=f"사유:{msg}.",color = 0xff0000))
            await user.ban()
        else:
            await message.channel.send(embed = Embed(title="권한이 없어요",color=0xff0000))
    
    if message.content.startswith(f"{p}버튼"):
        await message.channel.send("안녕",view = org_but())
    
    if message.content.startswith(f"{p}추가"):
        if message.author.guild_permissions.administrator or message.author.id == scratcher:
            user = message.mentions[0]
            await user.add_roles(utils.get(message.guild.roles,id = int((str(message.content).split("<@&")[1]).split(">")[0])))
            await message.channel.send(embed = Embed(title = "역할추가!",description = "{}님에게서 **{}** 역할을 추가했어요".format(user.mention,utils.get(message.guild.roles,id = int((str(message.content).split("<@&")[1]).split(">")[0]))),color = 0x00ff00))
        else:
            await message.channel.send(embed = Embed(title = "권한이 없어요!",description="__역할관리__ 권한이 필요합니다",color = 0xff0000))
    if message.content.startswith(f"{p}제거"):
        if message.author.guild_permissions.administrator or message.author.id == scratcher:
            user = message.mentions[0]
            await user.remove_roles(utils.get(message.guild.roles,id = int((str(message.content).split("<@&")[1]).split(">")[0])))
            await message.channel.send(embed = Embed(title = "역할제거!",description = "{}님에게서 **{}** 역할을 제거했어요".format(user.mention,utils.get(message.guild.roles,id = int((str(message.content).split("<@&")[1]).split(">")[0]))),color = 0xff0000))
        else:
            await message.channel.send(embed = Embed(title = "권한이 없어요!",description="__역할관리__ 권한이 필요합니다",color = 0xff0000))
    
    if message.content.startswith(f"{p}이모지"):
        try:
            if "a" in str(str(message.content).split("<")[1].split(":")[0]):
                emoji = (str(message.content).split(":")[2]).replace(">","")
                emoji_link = f"https://cdn.discordapp.com/emojis/{emoji}.gif?size=160"
                await message.reply(emoji_link)
            else:
                emoji = (str(message.content).split(":")[2]).replace(">","")
                emoji_link = f"https://cdn.discordapp.com/emojis/{emoji}.png?size=160"
                await message.reply(emoji_link)
        except:
            await message.reply(embed = Embed(title = "오류!",description = "커스텀 이모지가 아닌거 같습니다",color = 0xff0000))
    
    if message.content.startswith(f"{p}봇") and ("봇정보" in str(message.content)) == False:
        try:
            bot = message.mentions[0]
            if bot.bot:
                req = requests.get(f"https://koreanbots.dev/api/v2/bots/{bot.id}").json()
                if req['data']['status'] == "online": a = "<:online:918491083527311370>"
                elif req['data']['status'] == "idle": a = "<:idle:918492422701457449>"
                elif req['data']['status'] == "dnd": a = "<:dnd:918492948667175012>"
                elif req['data']['status'] == "streaming": a = "<:live:918278975908905001>"
                elif req['data']['status'] == "offline": a = "<:offline:918490930699456563>"
                embed = Embed(title=f"{bot} {a} 봇의 정보",color = random_color())
                embed.add_field(name = "접두사",value = f">>> {req['data']['prefix']}",inline=False)
                embed.add_field(name = "소유자",value = f">>> {req['data']['owners'][0]['username']}",inline=False)
                embed.add_field(name = "라이브러리",value = f">>> {req['data']['lib']}",inline=False)
                embed.add_field(name = "하트수",value = f">>> {req['data']['votes']}",inline=False)
                embed.add_field(name = "설명",value = f">>> {req['data']['desc']}",inline=False)
                embed.add_field(name = "봇초대",value = f">>> [클릭하기]({(req['data']['url'])})",inline=False)
                embed.add_field(name = "서버초대",value = f">>> [클릭하기](https://discord.com/invite/{(req['data']['discord'])})",inline=False)
                print(req['data']['bg'])
                
                await message.channel.send(embed = embed)
            else:
                await message.channel.send(embed = Embed(title="오류!",description="봇이 아니에요!",color = 0xff0000))
        except:
            await message.channel.send(embed = Embed(title="오류!",description="봇이 [한국 디스코드봇 리스트](https://koreanbots.dev/) 에 없어요",color = 0xff0000))
        
    if message.content.startswith(f"{p}요청"):
        msg_send = "yes"
        def check(m):
            return m.author.id == message.author.id

        a = await message.reply(embed = Embed(color=random_color() , title = "채널 이름을 써주세요" , description="취소하고 싶다면 ``취소``를 보내주세요\n[사용방법](https://youtu.be/QEji3fu1D88)"))
        msg = await client.wait_for("message" , check=check)
        name = str(msg.content)
        name_lower = name.lower()
        if msg.content == "취소":
            await a.delete()
            msg_send = "no"

        await a.edit(embed = Embed(color=random_color() , title = "짧은 설명을 쓰세요" , description="취소하고 싶다면 ``취소``를 보내주세요\n[사용방법](https://youtu.be/QEji3fu1D88)"))
        msg = await client.wait_for("message" , check=check)
        short_description = str(msg.content)
        if msg.content == "취소":
            await a.delete()
            msg_send = "no"

        await a.edit(embed = Embed(color=random_color() , title = "길은 설명을 쓰세요" , description="취소하고 싶다면 ``취소``를 보내주세요\n[사용방법](https://youtu.be/QEji3fu1D88)"))
        msg = await client.wait_for("message" , check=check)
        description = str(msg.content)
        if msg.content == "취소":
            await a.delete()
            msg_send = "no"

        await a.edit(embed = Embed(color=random_color() , title = "채널 링크를 쓰세요" , description="취소하고 싶다면 ``취소``를 보내주세요\n[사용방법](https://youtu.be/QEji3fu1D88)"))
        msg = await client.wait_for("message" , check=check)
        link = str(msg.content)
        try:
            await msg.delete()
        except:
            pass
        if msg.content == "취소":
            await a.delete()
            msg_send = "no"

        await a.edit(embed = Embed(color=random_color() , title = "채널 이미지 링크를 쓰세요 또는 이미지를 보내세요" , description="취소하고 싶다면 ``취소``를 보내주세요\n[사용방법](https://youtu.be/QEji3fu1D88)"))
        msg = await client.wait_for("message" , check=check)
        try:
            img = str(msg.attachments[0])
        except:
            img = str(msg.content)
        if msg.content == "취소":
            await a.delete()
            msg_send = "no"
            
        await a.edit(embed = Embed(color=random_color() , title = "디스코드 채널 링크를 쓰세요 없으면 None" , description="취소하고 싶다면 ``취소``를 보내주세요\n[사용방법](https://youtu.be/QEji3fu1D88)"))
        msg = await client.wait_for("message" , check=check)
        discord = msg.content
        try:
            await msg.delete()
        except:
            pass
        if msg.content == "취소":
            await a.delete()
            msg_send = "no"
        short_description = short_description.replace("\n","\\n")
        description = description.replace("\n","\\n")
        json_message = f'''
```json
"{name_lower}" : [
    "name": "{name}",
    "short_description" : "{short_description}",
    "description": "{description}",
    "img": "{img}",
    "channel": "{link}",
    "discord": "{discord}",
    "heart": "0",
    "tag": "0",
    "tsgs": "0"
]
```'''.replace("[","{").replace("]","}")
        await a.edit(embed = Embed(title = "전송완료" , description = json_message))
        if msg_send == "yes":
            await client.get_channel(923831470219493376).send(embed = Embed(color = random_color() , title="유튜버 추가요청!",description=f"{json_message}\n>>> id : {message.author.id}\nname : {message.author}"))

    if message.content.startswith(f"{p}업타임"):
        await message.channel.send(embed = Embed(title = "업타임!" , description=f"``{uptime_d}일 {uptime_h}시간 {uptime_m}분 {uptime_s}초`` 동안 리셋안하고 작동중"))

    if message.content.startswith(f"{p}끝말잇기"):
        async with message.channel.typing():
            key = "43F2B9D4EC883263F878DC81295B8E60"
            try:
                with open("randomText.json","r+") as f:
                    text = json.load(f)
                    text = text["1"][randint(0,len(text["1"])-1)]
            except:
                text = "시작"
                
            a = requests.get(f"https://stdict.korean.go.kr/api/search.do?key={key}&req_type=json&q={text}").json()

            word = a["channel"]["item"][0]["word"]
            description = a["channel"]["item"][0]["sense"]["definition"]
            link = a["channel"]["item"][0]["sense"]["link"]

            embedMessage = await message.channel.send(embed = Embed(title = f"**{message.author}**님이 소환함" , description = f"단어 : **{word}**\n\n뜻 : {description} \n\n[국어사전]({link})" , color = random_color() ) , view = rmx_button())
            def check(m):
                return (m.channel.id == message.channel.id)
        
        async def rmx(embedMessage):
            msg = await client.wait_for("message" , check=check)
            if (msg != "끝말잇기를 종료하셨습니다.") and (msg.author.bot == False):
                re = await msg.reply(">>> 확인중.")
                key = "43F2B9D4EC883263F878DC81295B8E60"
                text = msg.content
                if text[0] == embedMessage.embeds[0].description.split("**")[1][len(embedMessage.embeds[0].description.split("**")[1])-1]:
                    async with message.channel.typing():

                        try:
                            a = requests.get(f"https://stdict.korean.go.kr/api/search.do?key={key}&req_type=json&q={text}").json()
                            nope = 0
                            await re.delete()
                        except:
                            nope = 1
                            await re.edit(">>> 없는단어 입니다")

                        if nope == 0:
                            word = a["channel"]["item"][0]["word"]
                            description = a["channel"]["item"][0]["sense"]["definition"]
                            link = a["channel"]["item"][0]["sense"]["link"]
                            embedMessage2 = await message.channel.send(embed = Embed(title = f"{embedMessage.embeds[0].title}" , description = f"단어 : **{word}**\n\n뜻 : {description} \n\n[국어사전]({link})" , color = random_color() ) , view = rmx_button())
                            await embedMessage.delete()
                            await rmx(embedMessage2)
                        else:
                            await rmx(embedMessage)
                else:
                    await rmx(embedMessage)
        await rmx(embedMessage)
        
    if message.content.startswith(f"{p}계산기"):
        await message.reply(embed = Embed(description = "```\nㅤ\n```" , color = random_color()) , view = calculator(message.author))
    
    if message.content.startswith(f"{p}그림"):
        try:size = int(message.content.replace(f"{p}그림",""))
        except:size = 10
        MainMap = []
        for i in range(size):
            map = []
            for j in range(size):
                map.append(randint(0 , 0))
            MainMap.append(map)
        MainMap[randint(0,size-1)][randint(0,size-1)] = 2
        await message.reply(embed = Embed(description = f"```\n{await DrowMapLoad(MainMap)}\n```" , color = random_color()) , view = drow(message.author , MainMap))

#게임-----------------------------------------------------------------------------------------------------------
    if message.content.startswith(f"{p}개발자") or message.content.startswith(f"{p}hellothisisverification"):
        await message.channel.send(embed = Embed(title="개발자 : SCRATCHER 5-23♪#9017",description = "개발자서버 : http://discord.5-23.kro.kr/\n봇초대 : http://discord.5-23bot.kro.kr/"))
#-----------------------------!명령어----------------------------#
    if message.content.startswith(f"{p}명령어"):
        embed = Embed(title = "명령어",color = 0x00ff00)
        embed.add_field(name="기본 명령어 - 1",value=f"""
>>> {p}수학
{p}업타임
{p}투표 /이름/항목1/항목2/항목3....
{p}정보
{p}타이머 초
{p}현재
{p}유튜브 채널이름
{p}서버정보
{p}활성화여부
{p}이모지 커스텀이모지
{p}봇 @봇 멘션
{p}요청 [한국 유튜버리스트](https://site-main.scratcher5-23.repl.co) 에 유튜버 추가를 요청함
""" , inline = False)
        embed.add_field(name="게임 명령어",value=f"""
>>> {p}벌기
{p}도박 숫자
{p}레벨 (@멘션)
{p}상점
{p}입금 @멘션
{p}참가
{p}끝말잇기
""" , inline = False)
        embed.add_field(name="권한필요 명령어",value=f"""
>>> {p}공지 /이름/글 ```어드민 필요```
{p}슬로우 초 ```어드민필요```
{p}링크 비활성화 #링크삭제 비활성화 ```어드민 필요```
{p}링크 활성화 #링크삭제 활성화 ```어드민 필요```
{p}킥 @멘션 사유 ```유저킥 필요```
{p}밴 @멘션 사유 ```유저밴 필요```
{p}추가 @멘션 @역할 ```어드민```
{p}제거 @멘션 @역할 ```어드민```
""" , inline = False)
        embed.add_field(name="삭제 명령어",value=f"""
>>> {p}청소 숫자 ```메세지관리 필요```
{p}clear 숫자 ```메세지관리 필요```
""" , inline = False)
        embed.add_field(name="음악 명령어",value=f"""
>>> {p}들어와
{p}나가
{p}재생 url
{p}정지
""" , inline = False)
        embed.add_field(name="버튼 명령어",value=f"""
>>> {p}버튼
{p}계산기
""" , inline = False)
        embed.add_field(name="셀렉트 명령어",value=f"""
>>> {p}봇정보
""" , inline = False)
        embed.add_field(name="AI",value=f"""
>>> //단어 ```핑퐁 빌더 지원```
""" , inline = False)
        embed.add_field(name="개발자 명령어",value=f"""
>>> {p}답변 @멘션/내용
{p}답장 @멘션/내용
""" , inline = False)
        embed.set_footer(text="개발자:SCRATCHER 5-23♪#9017", icon_url="https://cdn.discordapp.com/icons/850364325834391582/86fe24d9e32bed450f822f0bc72a729b.png?size=96")
        await message.channel.send(embed = embed)
    

#--------------------------------------음악--------------------------------------#

    if message.content.startswith(f"{p}상태"):
        await message.channel.send("""🟢│음악명령어 사용가능""")

    if message.content.startswith(f"{p}들어와"):
        await message.author.voice.channel.connect()
        await message.delete()

    if message.content.startswith(f"{p}나가"):
        for vc in client.voice_clients:
            if vc.guild == message.guild:
                voice = vc
        await voice.disconnect()
        await message.delete()

    if message.content.startswith(f"{p}재생"):
        noo = 0
        embed = Embed(title = f"{message.author.name}님이요청하신 곡을 준비중 입니다", color = 0x00ff00)
        emb = await message.channel.send(embed = embed)
        for vc in client.voice_clients:
            if vc.guild == message.guild:
                voice = vc
        channel = message.author.voice.channel
        txt = message.content[4:]
        print(txt)
        res = requests.get(f"https://youtube.googleapis.com/youtube/v3/search?q={txt}&part=snippet&type=veodio&key={yt_api_key_m}&alt=json",headers={'User-Agent': 'Mozilla/5.0'}).json()
        for item in sorted(res['items'] , key=lambda x:x['snippet']['publishedAt']):
            title = item['snippet']['title']
            img = item['snippet']['thumbnails']['high']['url']
            try:
                url = f"https://www.youtube.com/watch?v={item['id']['videoId']}"
            except:
                await emb.edit(embed = Embed(title = "오류!",description = "곡을 찾을수 없어요",color = 0xff0000))
                noo = 1
                break
            break
        if noo == 0:
            ydl_opts = {'format': 'bestaudio'}
            FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            with YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                URL = info['formats'][0]['url']
                name = info['title']
            voice = client.voice_clients[0]
            if not vc.is_playing():
                embed = Embed(title = f"{message.author.name}님이 {name}을 재생합니다" , color = 0x00ff00 , description = f"[유튜브영상링크]({url})")
                embed.set_thumbnail(url = img)
                a = await emb.edit(embed = embed)
                await a.add_reaction("<:vv:905014667632594994>")
            else:
                await a.delete()
                await message.channel.send(embed = Embed(title = "이미 다른곡이 재생중 입니다" , description = "곡을 멈추고 싶다면 ``5정지``를 사용하세요"))
            if not vc.is_playing():
                # musicPlay(URL , voice , FFMPEG_OPTIONS)
                voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))

    
    if message.content.startswith(f"{p}정지"):
        for vc in client.voice_clients:
          if vc.guild == message.guild:
              voice = vc
        voice.stop()
        await message.delete()
    try:
        f.close()
    except:
        pass

#--------------------------------------음악--------------------------------------#

    if message.content.startswith(f"{p}링크 비활성화"):
        if message.author.guild_permissions.manage_messages or message.author.id == scratcher:
            f = open("svr.txt","r")
            svr_list = f.read().split("|")
            for i in range(len(svr_list)+1):
                try:
                    if str(message.guild.id) == str(svr_list[i]):
                        svr_on = 0
                        break
                    else:
                        svr_on = 1
                except:
                    pass
            if svr_on == 1:
                f.close()
                f = open("svr.txt","r")
                svr_txt = f.readline()
                f.close()
                f = open("svr.txt","w")
                f.write((str(svr_txt)+str(message.guild.id)+"|").replace("||","|"))
                f.close()
                await message.reply("비활성화 완료")
            else:
                print("nope")
                await message.reply("이미 비활성화 되있어요")
        else:
            await message.reply("권한이 없어요")

    if message.content.startswith(f"{p}링크 활성화"):
        if message.author.guild_permissions.manage_messages or message.author.id == scratcher:
            f = open("svr.txt","r")
            svr_list = f.read().split("|")
            for i in range(len(svr_list)+1):
                try:
                    if str(message.guild.id) == str(svr_list[i]):
                        svr_on = 0
                        svr_line = i
                        break
                    else:
                        svr_on = 1
                except:
                    pass
            if svr_on == 0:
                f.close()
                f = open("svr.txt","r")
                svr_list = f.readline().split("|")
                f.close()
                f = open("svr.txt","w")
                svr_list[svr_line] = ""
                svr_txt = (((((str(svr_list).replace(",","|")).replace("'","")).replace("[","")).replace("]","")).replace(" ","")).replace("||","|")
                f.write(svr_txt)
                f.close()
                await message.reply("활성화 했어요!")
            else:
                print("nope")
                await message.reply("이미 활성화 되있어요")
        else:
            await message.reply("권한이 없어요")
        
    if message.content.startswith(f"{p}활성화여부"):
        msg = await message.channel.send(embed = Embed(title="활성화여부"))
        f1 = open("svr.txt","r")
        if str(message.guild.id) in str(f1):
            await msg.edit(embed = Embed(title="활성화여부",description="링크삭제 비활성화됨"))
        else:
            await msg.edit(embed = Embed(title="활성화여부",description="링크삭제 활성화됨"))
        f1.close()
    
#----------------리액션-----------------#
@client.event
async def on_reaction_remove(reaction, user):
    message = reaction.message
    if str(reaction.emoji) == "👁":
        if user.guild_permissions.manage_messages:
            if message.author.id == five:
                if str(message.embeds[0].title) == "추가 완료!" or str(message.embeds[0].title) == "제거 완료!":
                    embed = Embed(title = message.embeds[0].title , color = message.embeds[0].color , description=f"메세지 관리자는 👁을 눌러서 금지단어를 보실수 있어요")
                    await message.edit(embed = embed)
@client.event
async def on_reaction_add(reaction, user):
    global five
    message = reaction.message

    if user.bot == False:


        if str(reaction.emoji) == "<:xx:905014703577772063>":
            if user.guild_permissions.manage_messages:
                if ("https://" in message.content or "http://" in message.content) and (("tenor.co" in message.content) == False and ("media.discordapp.net" in message.content) == False and ("https://cdn.discordapp.com/emojis/" in message.content) == False):
                    await reaction.message.author.send(embed = Embed(title = "메세지 삭제",description = f"{user}님의의해 당신의 [링크]({reaction.message.content}) 가 삭제되었습니다"))
                    await reaction.message.delete()
#버튼------------------------------------------------------
class org_but(ui.View):
    @ui.button(label="버튼",style=ButtonStyle.green)
    async def sub(self,bt:ui.Button,inter:Integration):
        await inter.response.send_message("ㅋㅋ",ephemeral = True)
        self.value = True

class rmx_button(ui.View):
    @ui.button(label = "끝내기" , style = ButtonStyle.red)
    async def rmx(self , button : ui.Button , inter : Integration):
        if inter.message.embeds[0].title.split("**")[1] == str(inter.user):
            await inter.message.delete()
            await inter.message.channel.send("끝말잇기를 종료하셨습니다.")
        else:
            await inter.response.send_message(">>> 자신의 것만 지울수 있어요" , ephemeral = True)
    
async def DownImg(url):
    return requests.get(url).content

class DownEmoji(ui.View):
    def __init__(self , url = None , user = None , name = None):
        self.url = url
        self.user = user
        self.name = name
        super().__init__(timeout=60)
    @ui.select(options = [SelectOption(label = "서버에 추가" , emoji = "<:plus:911643433653923880>" , description="선택한 이모지를 서버에 추가합니다"),SelectOption(label = "메세지 삭제" , emoji = "<:delete:911635798602952704>" , description="선택한 메세지를 삭제합니다"),SelectOption(label = "다른 이모지 보기" , emoji = "<:edit:911643433603596308>" , description="다른 이모지를 찾습니다"),SelectOption(label = "끝내기" , emoji = "<:channel_lock:911651516962725979>" , description="이모지  찾기를 끝냅니다")])
    async def Down(self , select : ui.Select , inter : Integration):
        if inter.user == self.user:
            if select.values[0] == "서버에 추가":
                if inter.user.guild_permissions.manage_emojis_and_stickers:
                    img = await DownImg(self.url)
                    await inter.guild.create_custom_emoji(name = self.name , image = img)
                    await inter.response.send_message("추가를 완료하였습니다!" , ephemeral = True)
                else:
                    await inter.response.send_message("이모지와 스티커 관리가 필요합니다" , ephemeral = True)
            if select.values[0] == "메세지 삭제":
                await inter.message.delete()
            
            if select.values[0] == "다른 이모지 보기":
                def emojiLoop():
                    global emojis
                    try:
                        guilds = client.guilds[randint(0,len(client.guilds)-1)]
                        emojis = guilds.emojis[randint(0,len(guilds.emojis)-1)]
                    except:
                        emojiLoop()
                emojiLoop()
                if "a" in str(str(emojis).split("<")[1].split(":")[0]):
                    emoji = (str(emojis).split(":")[2]).replace(">","")
                    emoji_link = f"https://cdn.discordapp.com/emojis/{emoji}.gif?size=160"
                else:
                    emoji = (str(emojis).split(":")[2]).replace(">","")
                    emoji_link = f"https://cdn.discordapp.com/emojis/{emoji}.png?size=160"
            
                    color = inter.message.embeds[0].color
                    await inter.message.edit(embed = Embed(title = f"이모지! {emojis}" , color = color).set_image(url =  emoji_link) , view = DownEmoji(user = inter.user , url = emoji_link , name = str(emojis).replace("<","").replace(">","").split(":")[1]))

            if select.values[0] == "끝내기":
                select.disabled = True

                await inter.message.edit(embed = inter.message.embeds[0] , view = self)

        else:
            await inter.response.send_message("자신의것을 사용하세요" , ephemeral = True)

async def Calculator(x):
    return eval(str(x).replace("```","").replace("\n","").replace("ㅤ","").replace("×","*").replace("÷","/").replace("²","**2").replace("𝝅","3.141592"))
class calculator(ui.View):
    def __init__(self , user):
        super().__init__(timeout=None)
        self.user = user

    @ui.button(label = "1" , style = ButtonStyle.gray)
    async def one(self , button : ui.Button , inter : Integration):
        if inter.user == self.user:
            integer = (str(inter.message.embeds[0].description).replace("```","").replace("\n","").replace("ㅤ",""))+str(button.label)
            await inter.message.edit(embed = Embed(description = f"```\n{integer}\n```" , color = inter.message.embeds[0].color))
        else:await inter.response.send_message(">>> 자신의것을 사용하세요" , ephemeral = True)
    
    @ui.button(label = "2" , style = ButtonStyle.gray)
    async def two(self , button : ui.Button , inter : Integration):
        if inter.user == self.user:
            integer = (str(inter.message.embeds[0].description).replace("```","").replace("\n","").replace("ㅤ",""))+str(button.label)
            await inter.message.edit(embed = Embed(description = f"```\n{integer}\n```" , color = inter.message.embeds[0].color))
        else:await inter.response.send_message(">>> 자신의것을 사용하세요" , ephemeral = True)
    
    @ui.button(label = "3" , style = ButtonStyle.gray)
    async def three(self , button : ui.Button , inter : Integration):
        if inter.user == self.user:
            integer = (str(inter.message.embeds[0].description).replace("```","").replace("\n","").replace("ㅤ",""))+str(button.label)
            await inter.message.edit(embed = Embed(description = f"```\n{integer}\n```" , color = inter.message.embeds[0].color))
        else:await inter.response.send_message(">>> 자신의것을 사용하세요" , ephemeral = True)

    @ui.button(label = "×" , style = ButtonStyle.blurple)
    async def x(self , button : ui.Button , inter : Integration):
        if inter.user == self.user:
            integer = (str(inter.message.embeds[0].description).replace("```","").replace("\n","").replace("ㅤ",""))+str(button.label)
            await inter.message.edit(embed = Embed(description = f"```\n{integer}\n```" , color = inter.message.embeds[0].color))
        else:await inter.response.send_message(">>> 자신의것을 사용하세요" , ephemeral = True)

    @ui.button(label = "끝" , style = ButtonStyle.red)
    async def end(self , button : ui.Button , inter : Integration):
        if inter.user == self.user:
            await inter.message.delete()
        else:await inter.response.send_message(">>> 자신의것을 사용하세요" , ephemeral = True)

    @ui.button(label = "4" , style = ButtonStyle.gray)
    async def four(self , button : ui.Button , inter : Integration):
        if inter.user == self.user:
            integer = (str(inter.message.embeds[0].description).replace("```","").replace("\n","").replace("ㅤ",""))+str(button.label)
            await inter.message.edit(embed = Embed(description = f"```\n{integer}\n```" , color = inter.message.embeds[0].color))
        else:await inter.response.send_message(">>> 자신의것을 사용하세요" , ephemeral = True)
    
    @ui.button(label = "5" , style = ButtonStyle.gray)
    async def five(self , button : ui.Button , inter : Integration):
        if inter.user == self.user:
            integer = (str(inter.message.embeds[0].description).replace("```","").replace("\n","").replace("ㅤ",""))+str(button.label)
            await inter.message.edit(embed = Embed(description = f"```\n{integer}\n```" , color = inter.message.embeds[0].color))
        else:await inter.response.send_message(">>> 자신의것을 사용하세요" , ephemeral = True)
    
    @ui.button(label = "6" , style = ButtonStyle.gray)
    async def six(self , button : ui.Button , inter : Integration):
        if inter.user == self.user:
            integer = (str(inter.message.embeds[0].description).replace("```","").replace("\n","").replace("ㅤ",""))+str(button.label)
            await inter.message.edit(embed = Embed(description = f"```\n{integer}\n```" , color = inter.message.embeds[0].color))
        else:await inter.response.send_message(">>> 자신의것을 사용하세요" , ephemeral = True)
    
    @ui.button(label = "÷" , style = ButtonStyle.blurple)
    async def divide(self , button : ui.Button , inter : Integration):
        if inter.user == self.user:
            integer = (str(inter.message.embeds[0].description).replace("```","").replace("\n","").replace("ㅤ",""))+str(button.label)
            await inter.message.edit(embed = Embed(description = f"```\n{integer}\n```" , color = inter.message.embeds[0].color))
        else:await inter.response.send_message(">>> 자신의것을 사용하세요" , ephemeral = True)
    
    @ui.button(label = "지우기" , style = ButtonStyle.red)
    async def delete(self , button : ui.Button , inter : Integration):
        if inter.user == self.user:
            integer = (str(inter.message.embeds[0].description).replace("```","").replace("\n","").replace("ㅤ",""))[:len((str(inter.message.embeds[0].description).replace("```","").replace("\n","")))-1]
            if integer == "":integer = "ㅤ"
            await inter.message.edit(embed = Embed(description = f"```\n{integer}\n```" , color = inter.message.embeds[0].color))
        else:await inter.response.send_message(">>> 자신의것을 사용하세요" , ephemeral = True)

    @ui.button(label = "7" , style = ButtonStyle.gray)
    async def seven(self , button : ui.Button , inter : Integration):
        if inter.user == self.user:
            integer = (str(inter.message.embeds[0].description).replace("```","").replace("\n","").replace("ㅤ",""))+str(button.label)
            await inter.message.edit(embed = Embed(description = f"```\n{integer}\n```" , color = inter.message.embeds[0].color))
        else:await inter.response.send_message(">>> 자신의것을 사용하세요" , ephemeral = True)
    
    @ui.button(label = "8" , style = ButtonStyle.gray)
    async def eight(self , button : ui.Button , inter : Integration):
        if inter.user == self.user:
            integer = (str(inter.message.embeds[0].description).replace("```","").replace("\n","").replace("ㅤ",""))+str(button.label)
            await inter.message.edit(embed = Embed(description = f"```\n{integer}\n```" , color = inter.message.embeds[0].color))
        else:await inter.response.send_message(">>> 자신의것을 사용하세요" , ephemeral = True)
    
    @ui.button(label = "9" , style = ButtonStyle.gray)
    async def nine(self , button : ui.Button , inter : Integration):
        if inter.user == self.user:
            integer = (str(inter.message.embeds[0].description).replace("```","").replace("\n","").replace("ㅤ",""))+str(button.label)
            await inter.message.edit(embed = Embed(description = f"```\n{integer}\n```" , color = inter.message.embeds[0].color))
        else:await inter.response.send_message(">>> 자신의것을 사용하세요" , ephemeral = True)
    
    @ui.button(label = "+" , style = ButtonStyle.blurple)
    async def plus(self , button : ui.Button , inter : Integration):
        if inter.user == self.user:
            integer = (str(inter.message.embeds[0].description).replace("```","").replace("\n","").replace("ㅤ",""))+str(button.label)
            await inter.message.edit(embed = Embed(description = f"```\n{integer}\n```" , color = inter.message.embeds[0].color))
        else:await inter.response.send_message(">>> 자신의것을 사용하세요" , ephemeral = True)

    @ui.button(label = "삭제" , style = ButtonStyle.red)
    async def deleteALL(self , button : ui.Button , inter : Integration):
        if inter.user == self.user:
            integer = "ㅤ"
            await inter.message.edit(embed = Embed(description = f"```\n{integer}\n```" , color = inter.message.embeds[0].color))
        else:await inter.response.send_message(">>> 자신의것을 사용하세요" , ephemeral = True)

    @ui.button(label = "0" , style = ButtonStyle.gray)
    async def zero(self , button : ui.Button , inter : Integration):
        if inter.user == self.user:
            integer = (str(inter.message.embeds[0].description).replace("```","").replace("\n","").replace("ㅤ",""))+str(button.label)
            await inter.message.edit(embed = Embed(description = f"```\n{integer}\n```" , color = inter.message.embeds[0].color))
        else:await inter.response.send_message(">>> 자신의것을 사용하세요" , ephemeral = True)
   
    @ui.button(label = "00" , style = ButtonStyle.gray)
    async def DoubleZero(self , button : ui.Button , inter : Integration):
        if inter.user == self.user:
            integer = (str(inter.message.embeds[0].description).replace("```","").replace("\n","").replace("ㅤ",""))+str(button.label)
            await inter.message.edit(embed = Embed(description = f"```\n{integer}\n```" , color = inter.message.embeds[0].color))
        else:await inter.response.send_message(">>> 자신의것을 사용하세요" , ephemeral = True)
    
    @ui.button(label = "." , style = ButtonStyle.gray)
    async def dot(self , button : ui.Button , inter : Integration):
        if inter.user == self.user:
            integer = (str(inter.message.embeds[0].description).replace("```","").replace("\n","").replace("ㅤ",""))+str(button.label)
            await inter.message.edit(embed = Embed(description = f"```\n{integer}\n```" , color = inter.message.embeds[0].color))
        else:await inter.response.send_message(">>> 자신의것을 사용하세요" , ephemeral = True)
    
    @ui.button(label = "-" , style = ButtonStyle.blurple)
    async def minus(self , button : ui.Button , inter : Integration):
        if inter.user == self.user:
            integer = (str(inter.message.embeds[0].description).replace("```","").replace("\n","").replace("ㅤ",""))+str(button.label)
            await inter.message.edit(embed = Embed(description = f"```\n{integer}\n```" , color = inter.message.embeds[0].color))
        else:await inter.response.send_message(">>> 자신의것을 사용하세요" , ephemeral = True)
    
    @ui.button(label = "=" , style = ButtonStyle.green)
    async def equal(self , button : ui.Button , inter : Integration):
        if inter.user == self.user:
            integer = await Calculator(inter.message.embeds[0].description)
            await inter.message.edit(embed = Embed(description = f"```\n{integer}\n```" , color = inter.message.embeds[0].color))
        else:await inter.response.send_message(">>> 자신의것을 사용하세요" , ephemeral = True)

    @ui.button(label = "(" , style = ButtonStyle.gray)
    async def open(self , button : ui.Button , inter : Integration):
        if inter.user == self.user:
            integer = (str(inter.message.embeds[0].description).replace("```","").replace("\n","").replace("ㅤ",""))+str(button.label)
            await inter.message.edit(embed = Embed(description = f"```\n{integer}\n```" , color = inter.message.embeds[0].color))
        else:await inter.response.send_message(">>> 자신의것을 사용하세요" , ephemeral = True)
    
    @ui.button(label = ")" , style = ButtonStyle.gray)
    async def cloose(self , button : ui.Button , inter : Integration):
        if inter.user == self.user:
            integer = (str(inter.message.embeds[0].description).replace("```","").replace("\n","").replace("ㅤ",""))+str(button.label)
            await inter.message.edit(embed = Embed(description = f"```\n{integer}\n```" , color = inter.message.embeds[0].color))
        else:await inter.response.send_message(">>> 자신의것을 사용하세요" , ephemeral = True)

    @ui.button(label = "x²" , style = ButtonStyle.gray)
    async def squared(self , button : ui.Button , inter : Integration):
        if inter.user == self.user:
            integer = (str(inter.message.embeds[0].description).replace("```","").replace("\n","").replace("ㅤ",""))+"²"
            await inter.message.edit(embed = Embed(description = f"```\n{integer}\n```" , color = inter.message.embeds[0].color))
        else:await inter.response.send_message(">>> 자신의것을 사용하세요" , ephemeral = True)
    
    @ui.button(label = "𝝅" , style = ButtonStyle.gray)
    async def pie(self , button : ui.Button , inter : Integration):
        if inter.user == self.user:
            integer = (str(inter.message.embeds[0].description).replace("```","").replace("\n","").replace("ㅤ",""))+str(button.label)
            await inter.message.edit(embed = Embed(description = f"```\n{integer}\n```" , color = inter.message.embeds[0].color))
        else:await inter.response.send_message(">>> 자신의것을 사용하세요" , ephemeral = True)

    @ui.button(label = "√" , style = ButtonStyle.gray)
    async def root(self , button : ui.Button , inter : Integration):
        if inter.user == self.user:
            integer = eval(str(inter.message.embeds[0].description).replace("```","").replace("\n","").replace("ㅤ",""))**(1/2)
            await inter.message.edit(embed = Embed(description = f"```\n{integer}\n```" , color = inter.message.embeds[0].color))
        else:await inter.response.send_message(">>> 자신의것을 사용하세요" , ephemeral = True)

async def DrowFind(x : list):
    for i in x:
        for j in i:
            if j == 2:
                return [x.index(i),i.index(2)]

async def DrowMapLoad(x):
    String = ""
    for i in x:
        for j in i:
            String += f"{j}"

        String += "\n"
    MainString = String.replace("0" , "⬜").replace("2" , "🟦")
    MainString = MainString.replace("1" , "⬛")
    return MainString


class drow(ui.View):
    def __init__(self , user , map):
        super().__init__(timeout=600)
        self.size = 10
        self.MainMap = map
        self.user = user
        self.emojiID = 1

    @ui.button(label = "↑" , style = ButtonStyle.blurple)
    async def w(self , button : ui.Button , inter : Integration):
        if inter.user == self.user:
            try:
                self.FindMap = await DrowFind(self.MainMap)
                self.MainMap[self.FindMap[0]][self.FindMap[1]] = self.emojiID
                self.MainMap[self.FindMap[0]-1][self.FindMap[1]] = 2
                await inter.message.edit(embed = Embed(description = f"```\n{await DrowMapLoad(self.MainMap)}\n```" , color = inter.message.embeds[0].color))
            except:
                await inter.message.edit(embed = Embed(description = f"```\n{await DrowMapLoad(self.MainMap)}\n```" , color = inter.message.embeds[0].color))
    
    @ui.button(label = "↓" , style = ButtonStyle.blurple)
    async def s(self , button : ui.Button , inter : Integration):
        if inter.user == self.user:
            try:
                self.FindMap = await DrowFind(self.MainMap)
                self.MainMap[self.FindMap[0]][self.FindMap[1]] = self.emojiID
                self.MainMap[self.FindMap[0]+1][self.FindMap[1]] = 2
                await inter.message.edit(embed = Embed(description = f"```\n{await DrowMapLoad(self.MainMap)}\n```" , color = inter.message.embeds[0].color))
            except:
                await inter.message.edit(embed = Embed(description = f"```\n{await DrowMapLoad(self.MainMap)}\n```" , color = inter.message.embeds[0].color))

    @ui.button(label = "←" , style = ButtonStyle.blurple)
    async def a(self , button : ui.Button , inter : Integration):
        if inter.user == self.user:
            try:
                self.FindMap = await DrowFind(self.MainMap)
                self.MainMap[self.FindMap[0]][self.FindMap[1]] = self.emojiID
                self.MainMap[self.FindMap[0]][self.FindMap[1]-1] = 2
                await inter.message.edit(embed = Embed(description = f"```\n{await DrowMapLoad(self.MainMap)}\n```" , color = inter.message.embeds[0].color))
            except:
                await inter.message.edit(embed = Embed(description = f"```\n{await DrowMapLoad(self.MainMap)}\n```" , color = inter.message.embeds[0].color))

    @ui.button(label = "→" , style = ButtonStyle.blurple)
    async def d(self , button : ui.Button , inter : Integration):
        if inter.user == self.user:
            try:
                self.FindMap = await DrowFind(self.MainMap)
                self.MainMap[self.FindMap[0]][self.FindMap[1]] = self.emojiID
                self.MainMap[self.FindMap[0]][self.FindMap[1]+1] = 2
                await inter.message.edit(embed = Embed(description = f"```\n{await DrowMapLoad(self.MainMap)}\n```" , color = inter.message.embeds[0].color))
            except:
                await inter.message.edit(embed = Embed(description = f"```\n{await DrowMapLoad(self.MainMap)}\n```" , color = inter.message.embeds[0].color))
    
    @ui.button(label="끝내기" , style = ButtonStyle.gray)
    async def rmx(self , button : ui.Button , inter : Integration):
        emoji = str(self.emojiID).replace("1","⬛").replace("0","⬜")
        await inter.message.edit(embed = Embed(description = str(inter.message.embeds[0].description).replace("🟦" , emoji) , color = inter.message.embeds[0].color) , view = None)
        

    @ui.button(label="⬛" , style = ButtonStyle.danger)
    async def black(self , button : ui.Button , inter : Integration):
        self.emojiID = 1
        await inter.message.edit(embed = inter.message.embeds[0])

    @ui.button(label="⬜" , style = ButtonStyle.danger)
    async def white(self , button : ui.Button , inter : Integration):
        self.emojiID = 0
        await inter.message.edit(embed = inter.message.embeds[0])

class vote1(ui.View):
    def __init__(self , title = None):
        super().__init__(timeout = None)
        self.title = title
        self.yesALL = []
        self.noALL = []

    @ui.button(emoji = "<:good:905078721881452565>" , style = ButtonStyle.green)
    async def yes(self , button : ui.Button , inter : Integration):
        if ((inter.user.id in self.yesALL) == False):
            try:self.noALL.remove(inter.user.id)
            except:pass

            try:self.yesALL.append(inter.user.id)
            except:pass

            description = f"<:good:905078721881452565> | {len(self.yesALL)}\n<:nooo:905078780421369946> | {len(self.noALL)}"
            embed = Embed(title = self.title , description = description , color = inter.message.embeds[0].color)
            await inter.message.edit(embed = embed)
        else:
            await inter.response.send_message("이미 <:good:905078721881452565>에 투표를 하였습니다" , ephemeral = True)
    @ui.button(emoji = "<:nooo:905078780421369946>" , style = ButtonStyle.red)
    async def no(self , button : ui.Button , inter : Integration):
        if ((inter.user.id in self.noALL) == False):
            try:self.noALL.append(inter.user.id)
            except:pass

            try:self.yesALL.remove(inter.user.id)
            except:pass

            description = f"<:good:905078721881452565> | {len(self.yesALL)}\n<:nooo:905078780421369946> | {len(self.noALL)}"
            embed = Embed(title = self.title , description = description , color = inter.message.embeds[0].color)
            await inter.message.edit(embed = embed)
        else:
            await inter.response.send_message(">>> 이미 <:nooo:905078780421369946>에 투표를 하였습니다" , ephemeral = True)

class urlButton(ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(ui.Button(label = "초대링크" , style = ButtonStyle.link , url = "https://discord.com/channels/949217844548235264/949217845160591422/949228008294723624" , emoji = "<:channel_store:936061731636133948>"))
        self.add_item(ui.Button(label = "어드민" , style = ButtonStyle.link , url = "https://discord.com/users/577266050769485844" , emoji = "<:setting:911307927367864350>"))

#버튼------------------------------------------------------



token = os.environ['BOT_TOKEN']
client.run(token)
