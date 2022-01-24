import os
import discord 

client = discord.client()
my_secret = os.environ['discord_key']

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format{client})


@client.event
async def on_message(message):
  if message.author == client.user:
  
    return 


  if message.content.startwith('$Hello'):
    await message.channel.send('Hello!')

  client.run(my_secret)

