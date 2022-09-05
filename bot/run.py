from os import getenv
import discord

from discord_logging import Logs

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

logs = Logs()

@client.event
async def on_ready():
    print('bot is running')

@client.event
async def on_thread_create(thread):
    print(thread.starting_message)
    await thread.join()

@client.event
async def on_message(message):
    # if(type(message.channel) == discord.threads.Thread):
        # print(message.channel.parent)
    logs.log_message(message)


client.run(getenv('token'))