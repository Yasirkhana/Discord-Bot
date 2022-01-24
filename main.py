import os
import discord 
import requests
import json



client = discord.Client()
my_secret = os.environ['discord_key']

def getquote():
  response = requests.get('https://zenquotes.io/api/random') 
  json_data = json.load(response.text)
  quote = json_data[0]['q'] + ' -'+ json_data[0]['a'] 
  print(quote)
  return(quote)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  


@client.event
async def on_message(message):
  if message.author == client.user:
    return 


  if message.content.startswith('$hi'):
    await message.channel.send(getquote())

client.run(my_secret)

