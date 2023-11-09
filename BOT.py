import discord
from discord import client
import openai
from discord.ext import commands
import os
from ai import chatgpt_response
import yt_dlp as youtube_dl
import youtube_dl
import asyncio
from discord.utils import get
from discord import FFmpegPCMAudio
from discord import TextChannel
from youtube_dl import YoutubeDL


intents = discord.Intents.default()
intents.message_content = True
 
TOKEN = 
openai.api_key = 
client = discord.Client(intents=intents)
#MUSIC
client = commands.Bot(command_prefix='?', intents=intents)  

players = {}





@client.event
async def on_ready():
    print("Bot is ready")


@client.event
#CHAT GPT BOT
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)

    print(username + " said " + user_message.lower() + " in " + channel)

    if message.channel.name == client.user:
        return
    command, user_message = None,None

    for text in ['/ai']:
      if message.content.startswith(text):
        command=message.content.split(" ")[0]
        user_message=message.content.replace(text, '')
        print(command, user_message)

    if command == '/ai':
      bot_response = chatgpt_response(prompt=user_message)
      await message.channel.send(f'Answer{bot_response}')


    #MUSIC
@client.command()
async def join(ctx):
      channel = ctx.message.author.voice.channel
      voice = get(client.voice_clients, guild=ctx.guild)
      if voice and voice.is_connected():
          await voice.move_to(channel)
      else:
          voice = await channel.connect()


  # command to play sound from a youtube URL
@client.command()
async def play(ctx, url):
      YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
      FFMPEG_OPTIONS = {
          'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
      voice = get(client.voice_clients, guild=ctx.guild)

      if not voice.is_playing():
        with YoutubeDL(YDL_OPTIONS, stderr=None) as ydl:
          
          info = ydl.extract_info(url, download=False)
          URL = info['url']
          voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
          voice.is_playing()
          await ctx.send('Bot is playing')

  # check if the bot is already playing
      else:
          await ctx.send("Bot is already playing")
          return


  # command to resume voice if it is paused
@client.command()
async def resume(ctx):
      voice = get(client.voice_clients, guild=ctx.guild)

      if not voice.is_playing():
          voice.resume()
          await ctx.send('Bot is resuming')


  # command to pause voice if it is playing
@client.command()

async def pause(ctx):
      voice = get(client.voice_clients, guild=ctx.guild)

      if voice.is_playing():
          voice.pause()
          await ctx.send('Bot has been paused')


  # command to stop voice
@client.command()
async def stop(ctx):
    
    voice = get(client.voice_clients, guild=ctx.guild)
  

    if voice.is_playing():
          voice.stop()
          await ctx.send('Stopping...')






client.run(TOKEN)
