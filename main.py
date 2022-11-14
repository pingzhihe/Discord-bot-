import discord
import os
import requests
import json
import random
from replit import db

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=discord.Intents.default())
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

starter_encouragements = [
  "Cheer up!", "Hang in there", "You are a great person / bot !"
]


def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " - " + json_data[0]['a']
  return quote


def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if message.content.startswith('$inspire'):
    print('get the text!')
    quote = get_quote()
    await message.channel.send(quote)

  if any(word in msg for word in sad_words):
    print('get the text!')
    await message.channel.send(random.choice(starter_encouragements))


client.run(os.getenv('TOKEN'))
