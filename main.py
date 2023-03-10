# -*- coding:utf-8 -*-

from time import sleep
import discord
import asyncio
import random
import requests
from datetime import datetime

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
  print("봇 실행됨!")
  print(client.user.name)
  print(client.user.id)
  await client.change_presence(activity=discord.Streaming(name="야동", url='https://www.youtube.com/watch?v=vdyFrWZv-dg'))

#명령어 입력구간
@client.event
async def on_message(message):
  if message.author.bot:
    return None


  if message.content == "!작동확인":
    await message.channel.send("작동중입니다")

  if message.content.startswith("!청소 "):
      purge_number = message.content.replace("!청소 ", "")
      check_purge_number = purge_number.isdigit()
      if check_purge_number == True:
          if message.author.guild_permissions.administrator:
            await message.channel.purge(limit=int(purge_number) + 1)
            msg = await message.channel.send(f"**{purge_number}개**의 메시지를 삭제했습니다.")
            await asyncio.sleep(5)
      else:
          await message.channel.send("꺼졍")

  if message.content == "!도박":
      gameb = '파산', '성공', '파산','파산','파산','파산','파산','파산','파산'
      result = random.choice(gameb)
      await message.channel.send(result)
      if result == '성공':
          await message.channel.send("그래봤자 넌 도박꾼이얌~")
          

  if message.content == "!주사위":
      dice = '1', '2', '3','4','5','6'
      result2 = random.choice(dice)
      await message.channel.send(result2)

  if message.content == "!후원":
      await message.channel.send("아래 암호화폐(LTC) 계좌로 입금하십시오.")
      await message.channel.send("LKmubo2rXnMtM1XMfRbhdiGXwE35qLxmut")
    
  if message.content =="!시간":
      now = datetime.now()
      s = now.strftime("%Y년-%m월-%d일 %H시%M분%S초")
      await message.channel.send(s)

client.run("token")
