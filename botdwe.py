import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")


@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.channel.send("응")
    if message.content.startswith("잘가"):
        await message.channel.send("또만나")
    if message.content.startswith("나야"):
        await message.channel.send("오우 심했다")
    if message.content.startswith("넌 나야"):
        await message.channel.send("넌 어반")
    if message.content.startswith("잘지내자"):
        await message.channel.send("응")

    if message.content.startswith("넌 누가만들어줬어?"):
        await message.channel.send("스타렉스 어반이(가)만들어줬어")
    if message.content.startswith("넌 누가 패치해줄거야?"):
        await message.channel.send("앞으로는 스타렉스 어반이(가)패치할거야")
    if message.content.startswith("알았어"):
        await message.channel.send("응")


access_token = os.environ["BOT_TOKEN"]
client.run(acces_token)
