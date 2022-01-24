import os
import discord 
import requests
import json
import random
from replit import db


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

def update_encouragement(encouraging_message):
  if "encouragements" in db.keys():
    encouragments  = db['encouragments']
    encouragments.append(encouraging_message)
    db["encouragments"] = encouragments
  else:
    db[encouragments] = [encouraging_message]

def delete_encouragement(index):
  encouragements = db['encouragements']
  if len(encouragements) > index:
    del encouragements[index]
    db['encouragements'] = encouragements



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

  options = starter_encouragements
  if "encouragements" in db.keys():
    options = options+ db['encouragements']

  elif any(word in msg for word in sad_words):
    await message.channel.send(random.choice(options))

  if msg.startswith('$new'):
    encouraging_message = msg.split("$new ",1)[1]
    update_encouragement(encouraging_message)
    await message.channel.send("New encouraging message added")

  if msg.startswith('$delete'):
    encouragments = []
    if 'encouragments' in db.keys():
      index = int(msg.split("$delete", 1)[1])
      delete_encouragement(index)
      encouragments = db['encouragments']
    await message.channel.send(encouragments)



  elif any(word in msg for word in wellcome_words):
    await message.channel.send('Your wellcome Sir :)')


client.run(my_secret)

