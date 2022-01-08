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

#to check weather
    if message.content.startswith('weather') or message.content.startswith('Weather') :
        channel = message.channel
        await channel.send('Enter the city name')

        
        city = await client.wait_for('message')
        url = api_adress + city.content
        json_data = requests.get(url).json()
        weather_des = json_data['weather'][0]['description']
        temp = json_data['main']['temp']


        await channel.send("In {} it's {} degree Faranheit with {}".format(city.content , temp , weather_des))


#accessing token
my_secret = os.environ['token new']#enter your token here
