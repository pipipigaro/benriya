import discord
import os
from discord.ext import commands
import random
import gspread
from google.oauth2.service_account import Credentials
import json
import asyncio
from discord.ext import commands, tasks

SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]
SPREADSHEET_NAME = '＊華灯＊管理表＊'
SHEET_NAME = '【生】アンケート回答'
SPREADSHEET_ID = '1mR1eTIdL6X_TrEljohV6mtFuupabNRxt1RloKH42gsQ'

service_account_info = json.loads(os.environ["GOOGLE_SHEET_CREDENTIALS"])
creds = Credentials.from_service_account_info(service_account_info, scopes=SCOPES)
gc = gspread.authorize(creds)
sheet = gc.open(SPREADSHEET_NAME).worksheet(SHEET_NAME)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!',intents=intents)
# スプレッドシート設定
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Google認証（Railwayの環境変数を使用）
creds_json = os.environ.get("GOOGLE_SHEET_CREDENTIALS")
creds_dict = json.loads(creds_json)
creds = Credentials.from_service_account_info(creds_dict, scopes=SCOPES)
gc = gspread.authorize(creds)
sheet = gc.open(SPREADSHEET_NAME).worksheet(SHEET_NAME)

mention_dict = {
    "えるる@SOP": "<@905502458413973544>",
    "ぽっちり": "<@835802888634236939>",
    "たらちゃん": "<@578261115029684235>",
    "エチ": "<@890415581243772978>",
    "はなみ": "<@937450425869815869>",
    "ろーぜ・まいん": "<@882486297174884412>",
    "AYA1": "<@857341252759584798>",
    "ピガロ": "<@920675593081733160>",
    "銀之助22": "<@878815180195250187>",
    "狂風": "<@436748567445635073>",
    "侑未": "<@989164799311110179>",
    "ルージェナ": "<@946552812987359263>",
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
    "エイトット": "<@878910220968026173>",
    "たまこちゃん": "<@831639349154152458>",
    "ぶらうんＪr": "<@966292802092806154>",
    "まるぼろん": "<@715545687898587219>",
    "ローストびーふ": "<@887714463812304936>",
    "＊ぷんぷん丸＊": "<@1307207181577490495>",
    "熱烈レモネード": "<@919448552357367828>",
    "悶絶辛辛魚": "<@919448879676657678>",
    "ゆーみす": "<@799922498778693692>",
    "＊リリィ＊＊": "<@884028070640631829>"
}


@bot.event
async def on_ready():
    print('便利屋が到着しました。')
    print(f'✅ Bot 起動完了: {bot.user}')
    collect_votes.start()

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
              winners_display = [
                  mention_dict.get(name.strip(), name.strip()) for name in winner_list
              ]
              winners_string = ', '.join(winners_display)
              await ctx.send(f'起死回生→ {winners_string} 入札忘れずに！')

@bot.command(name='キングダムスキル本')
async def lottery3(ctx, participants: str, winners: int):
          participants_list = participants.split(',')
          participants = ', '.join(participants_list)  # リストを文字列に変換
          if winners > len(participants_list):
              await ctx.send('当選数が参加者数を超えています。')
          else:
              winner_list = random.sample(participants_list, winners)
              winners_display = [
                  mention_dict.get(name.strip(), name.strip()) for name in winner_list
              ]
              winners_string = ', '.join(winners_display)
              await ctx.send(f'キングダムスキル本→ {winners_string} 入札忘れずに！')

@bot.command(name='王位スキル本')
async def lottery4(ctx, participants: str, winners: int):
          participants_list = participants.split(',')
          participants = ', '.join(participants_list)  # リストを文字列に変換
          if winners > len(participants_list):
              await ctx.send('当選数が参加者数を超えています。')
          else:
              winner_list = random.sample(participants_list, winners)
              winners_display = [
                  mention_dict.get(name.strip(), name.strip()) for name in winner_list
              ]
              winners_string = ', '.join(winners_display)
              await ctx.send(f'王位スキル本→ {winners_string} 入札忘れずに！')

@bot.command(name='ファイアブースト')
async def lottery5(ctx, participants: str, winners: int):
          participants_list = participants.split(',')
          participants = ', '.join(participants_list)  # リストを文字列に変換
          if winners > len(participants_list):
              await ctx.send('当選数が参加者数を超えています。')
          else:
              winner_list = random.sample(participants_list, winners)
              winners_display = [
                  mention_dict.get(name.strip(), name.strip()) for name in winner_list
              ]
              winners_string = ', '.join(winners_display)
              await ctx.send(f'ファイアブースト→ {winners_string} 入札忘れずに！')

@bot.command(name='ウッドブースト')
async def lottery6(ctx, participants: str, winners: int):
          participants_list = participants.split(',')
          participants = ', '.join(participants_list)  # リストを文字列に変換
          if winners > len(participants_list):
              await ctx.send('当選数が参加者数を超えています。')
          else:
              winner_list = random.sample(participants_list, winners)
              winners_display = [
                  mention_dict.get(name.strip(), name.strip()) for name in winner_list
              ]
              winners_string = ', '.join(winners_display)
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

@bot.command(name='侵攻戦')
async def shinkou(ctx):
    await create_poll(ctx, '侵攻戦')

@bot.command(name='遺物')
async def ibutsu(ctx):
    await create_poll(ctx, '遺物')

@bot.command(name='レイド')
async def raid(ctx):
    await create_poll(ctx, 'レイド')

# 絵文字と選択肢の辞書
EMOJI_OPTIONS = {'🇦': '参加', '🇧': '来れたら行く', '🇨': '不参加'}

# 最新アンケートメッセージ追跡
latest_messages = {}

async def create_poll(ctx, category):
    description = "\n".join([f"{emoji} {text}" for emoji, text in EMOJI_OPTIONS.items()])
    embed = discord.Embed(title=f"{category}アンケート", description=description, color=0x3498db)
    message = await ctx.send(embed=embed)

    for emoji in EMOJI_OPTIONS:
        await message.add_reaction(emoji)

    latest_messages[category] = message.id

@tasks.loop(minutes=180)
async def collect_votes():
    print("🔍 アンケート集計中...")
    for category, message_id in latest_messages.items():
        for guild in bot.guilds:
            for channel in guild.text_channels:
                try:
                    message = await channel.fetch_message(message_id)
                    await process_votes(message, category)
                    break
                except:
                    continue

async def process_votes(message, category):
    vote_map = {}

    for reaction in message.reactions:
        if reaction.emoji in EMOJI_OPTIONS:
            users = await reaction.users().flatten()
            for user in users:
                if user.bot:
                    continue
                vote_map[user.display_name] = EMOJI_OPTIONS[reaction.emoji]

    data = sheet.get_all_values()
    name_col = [row[0] for row in data]
    col_index = {'侵攻戦': 1, '遺物': 2, 'レイド': 3}[category]

    for name, answer in vote_map.items():
        if name in name_col:
            row_idx = name_col.index(name) + 1
            sheet.update_cell(row_idx + 1, col_index + 1, answer)
        else:
            sheet.append_row([
                name if category == '侵攻戦' else '',
                answer if category == '侵攻戦' else '',
                answer if category == '遺物' else '',
                answer if category == 'レイド' else ''
            ])
            
@bot.command(name='リセット')
async def reset_data(ctx, type_name: str):
    valid_types = ["侵攻戦", "遺物", "レイド"]
    if type_name not in valid_types:
        await ctx.send(f"無効な種類だよ！指定できるのは：{', '.join(valid_types)}")
        return

    col_index = {'侵攻戦': 2, '遺物': 3, 'レイド': 4}[type_name]  

    all_data = sheet.get_all_values()
    
    for row_idx in range(2, len(all_data)+1):
        sheet.update_cell(row_idx, col_index, '')

    await ctx.send(f"{type_name}のデータをリセットしました。")
    
def clear_data_by_type(sheet, type_name):
    all_data = sheet.get_all_values()
    headers = all_data[0]
    rows = all_data[1:]

    # 種類の列（headers[1]）がtype_nameと一致する行を除外する
    new_rows = [row for row in rows if len(row) < 2 or row[1] != type_name]

    sheet.clear()
    sheet.append_row(headers)
    for row in new_rows:
        sheet.append_row(row)

@bot.command(name='集計')
async def force_collect(ctx, category: str):
    category = category.strip()
    if category not in ['侵攻戦', '遺物', 'レイド']:
        await ctx.send("カテゴリは「侵攻戦」「遺物」「レイド」のいずれかで指定してください。")
        return

    if category not in latest_messages:
        await ctx.send(f"{category}のアンケートメッセージが見つかりません。")
        return

    for guild in bot.guilds:
        for channel in guild.text_channels:
            try:
                message = await channel.fetch_message(latest_messages[category])
                await process_votes(message, category)
                await ctx.send(f"{category}の集計を実行しました。")
                return
            except:
                continue
    await ctx.send(f"{category}のメッセージを取得できませんでした。")

TOKEN = os.getenv("DISCORD_TOKEN")
if TOKEN is None:
    raise ValueError("DISCORD_TOKEN が設定されていません。")

try:
    bot.run(TOKEN)
except Exception as e:
    print(f"Bot起動に失敗: {e}")
