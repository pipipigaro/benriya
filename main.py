import discord
import os
from discord.ext import commands
import random

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_ready():
    print('便利屋が到着しました。')

@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

@bot.command(name='抽選')
async def lottery1(ctx, participants: str, winners: int):
          participants_list = participants.split(',')
          participants = ', '.join(participants_list)  # リストを文字列に変換
          if winners > len(participants_list):
              await ctx.send('当選数が参加者数を超えています。')
          else:
              winner_list = random.sample(participants_list, winners)
              winners_string = ', '.join(winner_list)
              await ctx.send(f'当選者→ {winners_string} 入札忘れずに！')

@bot.command(name='起死回生')
async def lottery2(ctx, participants: str, winners: int):
          participants_list = participants.split(',')
          participants = ', '.join(participants_list)  # リストを文字列に変換
          if winners > len(participants_list):
              await ctx.send('当選数が参加者数を超えています。')
          else:
              winner_list = random.sample(participants_list, winners)
              winners_string = ', '.join(winner_list)
              await ctx.send(f'起死回生→ {winners_string} 入札忘れずに！')

@bot.command(name='キングダムスキル本')
async def lottery3(ctx, participants: str, winners: int):
          participants_list = participants.split(',')
          participants = ', '.join(participants_list)  # リストを文字列に変換
          if winners > len(participants_list):
              await ctx.send('当選数が参加者数を超えています。')
          else:
              winner_list = random.sample(participants_list, winners)
              winners_string = ', '.join(winner_list)
              await ctx.send(f'キングダムスキル本→ {winners_string} 入札忘れずに！')

@bot.command(name='王位スキル本')
async def lottery4(ctx, participants: str, winners: int):
          participants_list = participants.split(',')
          participants = ', '.join(participants_list)  # リストを文字列に変換
          if winners > len(participants_list):
              await ctx.send('当選数が参加者数を超えています。')
          else:
              winner_list = random.sample(participants_list, winners)
              winners_string = ', '.join(winner_list)
              await ctx.send(f'王位スキル本→ {winners_string} 入札忘れずに！')

@bot.command(name='ファイアブースト')
async def lottery5(ctx, participants: str, winners: int):
          participants_list = participants.split(',')
          participants = ', '.join(participants_list)  # リストを文字列に変換
          if winners > len(participants_list):
              await ctx.send('当選数が参加者数を超えています。')
          else:
              winner_list = random.sample(participants_list, winners)
              winners_string = ', '.join(winner_list)
              await ctx.send(f'ファイアブースト→ {winners_string} 入札忘れずに！')

@bot.command(name='ウッドブースト')
async def lottery6(ctx, participants: str, winners: int):
          participants_list = participants.split(',')
          participants = ', '.join(participants_list)  # リストを文字列に変換
          if winners > len(participants_list):
              await ctx.send('当選数が参加者数を超えています。')
          else:
              winner_list = random.sample(participants_list, winners)
              winners_string = ', '.join(winner_list)
              await ctx.send(f'ウッドブースト→ {winners_string} 入札忘れずに！')

@bot.command(name='抽選方法')
async def question(ctx):
    await ctx.send('''
    !(抽選したい本の名称)_参加者1,参加者2,…_当選数
_部分は空白
参加者は,(カンマ)区切り
最後の参加者の後にカンマは付けない
''')

TOKEN = os.getenv("DISCORD_TOKEN")
if TOKEN is None:
    raise ValueError("DISCORD_TOKEN が設定されていません。")

try:
    bot.run(TOKEN)
except Exception as e:
    print(f"Bot起動に失敗: {e}")
