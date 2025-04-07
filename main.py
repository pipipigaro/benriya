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
    # ニックネームとメンションIDの対応辞書
    mention_dict = {
        "えるる@SOP": "<@eruru9304>",
        "ぽっちり": "<@pochiri.>",
        "たらちゃん": "<@tarachan2493>",
        "エチ": "<@echi1212>",
        "はなみ": "<@hana7730>",
        "ろーぜ・まいん": "<@nanamarupesi>",
        "リアルん": "<@riarun_>",
        "AYA1": "<@aya7214>",
        "ピガロ": "<@_pigaro_>",
        "銀之助22": "<@ginnosuke222>",
        "狂風": "<@misheria_>",
        "侑未": "<@umi.1234>",
        "ルージェナ": "<@lu__jena>",
        "はっちゃん8": "<@hacchan8>",
        "燈花": "<@touka_2.28>",
        "鏡音月華": "<@gettka22>",
        "鬼Lua": "<@onmyojilua>",
        "るちぁ": "<@rupa3003>",
        "ライトネク": "<@raito_neku>",
        "はどう": "<@hadou0321>",
        "オリオンララ": "<@orionrara.>",
        "Kombucha": "<@kombucha0269>",
        "ハロベルト": "<@haroberuto>",
        "マインハート": "<@mine_heart>",
        "カールセフ": "<@karu0567>",
        "えりあ": "<@eria_iry>",
        "丹礼真": "<@kotonako1014>",
        "セラニオコ": "<@seraniocco>",
        "ジューンミナ": "<@junemina>",
        "Perdita": "<@perdita8243>",
        "もふにゃあ": "<@mo_funyaa>",
        "シェルロート": "<@shell0053_50234>",
        "ルゥ・チクク": "<@ruchiku>",
        "エイトット": "<@tto20>"
    }

    participants_list = participants.split(',')
    participants = ', '.join(participants_list)

    if winners > len(participants_list):
        await ctx.send('当選数が参加者数を超えています。')
    else:
        winner_list = random.sample(participants_list, winners)

        # メンションIDが登録されていればメンションで、なければ名前のまま表示
        winners_display = [
            mention_dict.get(name.strip(), name.strip()) for name in winner_list
        ]
        winners_string = ', '.join(winners_display)
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

@bot.command(name='投票')
async def vote(ctx, *, content: str):
    try:
        parts = content.split(',')
        if len(parts) < 2:
            await ctx.send("形式が正しくありません。例：!投票 好きな色は？,赤,青,緑")
            return

        question = parts[0].strip()
        choices = [choice.strip() for choice in parts[1:]]

        if len(choices) > 5:
            await ctx.send("選択肢は最大5つまでです。")
            return

        emojis = ['🇦', '🇧', '🇨', '🇩', '🇪']

        description = ""
        for i, choice in enumerate(choices):
            description += f"{emojis[i]} {choice}\n"

        embed = discord.Embed(title=question, description=description, color=0x3498db)
        message = await ctx.send(embed=embed)

        for i in range(len(choices)):
            await message.add_reaction(emojis[i])

    except Exception as e:
        await ctx.send(f"投票の作成に失敗しました: {e}")

TOKEN = os.getenv("DISCORD_TOKEN")
if TOKEN is None:
    raise ValueError("DISCORD_TOKEN が設定されていません。")

try:
    bot.run(TOKEN)
except Exception as e:
    print(f"Bot起動に失敗: {e}")
