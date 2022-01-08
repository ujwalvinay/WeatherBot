#importing discord api
import discord
import os
import requests
#to keep the bot alive from goin back to sleep , creating a server
from keepalive import keep_alive

#webadress of openweathermap
api_adress = '' #paste your api adress here till the &q= 
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
#for chit chat
    if message.content.startswith('hello') or message.content.startswith('Hello '):
        await message.channel.send("Hello , I'm Chatty !")
        await message.channel.send("How can I help you ?")

    if message.content.startswith('how are you') or message.content.startswith('How are you'):
        await message.channel.send("I'm Good , Thanks for asking !")

    if message.content.startswith('what can you do') or message.content.startswith('What can you do'):
        await message.channel.send("For starters I can check the weather \n Enter 'weather' to check weather ")

    if message.content.startswith('Who made you') or message.content.startswith('who made you'):
        await message.channel.send('A grad student named Ujwal')
#accessing token
my_secret = os.environ['token new']#enter your token here
