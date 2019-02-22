
import asyncio
import discord
import random


client = discord.Client()


token = "https://google.com"


@client.event
async def on_ready():
    print("logged in as :")
    print(client.user.name)
    print(client.user.id)
    print("------")

    await client.change_presence(game=discord.Game(name="심각한 고뇌중"))


@client.event
async def on_message(message):
    if message.author.bot:
        return None

    elif message.content == ("야"):
        await client.send_message(message.channel, "왜")
    
    elif message.content.endswith("지?"):
        await client.send_message(message.channel, random.choice(["아닌데?","당연하지","잘 몰라"]))
		
    elif message.content.endswith("까?"):
        await client.send_message(message.channel, random.choice(["아닌데?","당연하지","잘 몰라"]))

client.run(token)
