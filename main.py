import discord
import os
from discord.ext import commands
import random

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!',intents=intents)

mention_dict = {
    "えるる@SOP": "<@905502458413973544>",
    "ぽっちり": "<@835802888634236939>",
    "たらちゃん": "<@578261115029684235>",
    "エチ": "<@890415581243772978>",
    "はなみ": "<@937450425869815869>",
    "ろーぜ・まいん": "<@882486297174884412>",
    "リアルん": "<@997431717583388702>",
    "AYA1": "<@857341252759584798>",
    "ピガロ": "<@920675593081733160>",
    "銀之助22": "<@878815180195250187>",
    "狂風": "<@436748567445635073>",
    "侑未": "<@989164799311110179>",
    "ルージェナ": "<@946552812987359263>",
    "はっちゃん8": "<@1000054014144172032>",
    "燈花": "<@681486065231724646>",
    "鏡音月華": "<@882475397441257494>",
    "鬼Lua": "<@1002197601925468180>",
    "るちぁ": "<@867094778256556073>",
    "ライトネク": "<@878882414687031357>",
    "はどう": "<@1357654657844904078>",
    "オリオンララ": "<@989308452956426270>",
    "Kombucha": "<@1204046932687720450>",
    "ハロベルト": "<@1073978850796654763>",
    "マインハート": "<@919445385381044314>",
    "カールセフ": "<@941928121169506314>",
    "えりあ": "<@877902025210343434>",
    "丹礼真": "<@1188835712922042543>",
    "セラニオコ": "<@1144642724465758240>",
    "ジューンミナ": "<@774191152274472970>",
    "Perdita": "<@1061821687718486037>",
    "もふにゃあ": "<@928675381127557180>",
    "シェルロート": "<@1193923210043986060>",
    "ルゥ・チクク": "<@877914334997647391>",
    "エイトット": "<@878910220968026173>"
}


@bot.event
async def on_ready():
    print('便利屋が到着しました。')

@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

@bot.command(name='抽選')
async def lottery1(ctx, participants: str, winners: int):

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
