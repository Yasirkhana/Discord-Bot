import os
import discord 
import requests
import json
import random



client = discord.Client()
my_secret = os.environ['discord_key']

sad_words = ['sad',"depressed",'unhappy','angry']
wellcome_words = ['thanks', 'happy', 'bye']

starter_encouragements = [
  'cheer up', 'hang in there!',
  'You are a great person/ Bot',
  'Tesnion not Bae!'
] 

def getquote():
  response = requests.get('https://zenquotes.io/api/random')
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + ' -'+ json_data[0]['a'] 

  return(quote)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  


@client.event
async def on_message(message):
  if message.author == client.user:
    return 

  msg = message.content

  if message.content.startswith('sad'):
    quote = getquote()
    await message.channel.send(quote)

  elif any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encouragements))

  elif any(word in msg for word in wellcome_words):
    await message.channel.send('Your wellcome Sir :)')
client.run(my_secret)

