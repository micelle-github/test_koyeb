import discord
import os
from dotenv import load_dotenv

load_dotenv()  # .envファイルを読み込む
token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents().all()
client = discord.Client(intents=intents)



@client.event
async def on_message(message):
    if message.author == client.user:
        return

#テキスト送信
    if message.content == 'うづ':
        await message.channel.send("🤗")
        await message.channel.send(token)
        await message.channel.send(type(token))

#画像表示　(同一ディレクトリ内参照)
    elif message.content == '画像':
        await message.channel.send(file=discord.File('image.jpg'))



client.run(token)