import os
import discord
from funcs import retrieveFunction

disc_token = os.environ['discord_token'];


client = discord.Client();


@client.event
async def on_ready():
  print('We have logged in')


@client.event
async def on_message(message):
  channel = client.get_channel(911007016930144316)
  if message.author == client.user:
    return
  if message.content.startswith("$test"):
    await channel.send("Test Success")
  if message.content.startswith('$retrieve'):
    tickers = message.content.split()
    tickers.pop(0)
    await channel.send(tickers)







client.run(disc_token);