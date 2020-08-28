import discord
import asyncio
import humanreadable as hr
import json

client = discord.Client()
uid = 0
try:
    with open('userconfig.json', 'w') as f:
        cfg = json.load(f)
        channels = cfg["channels"]

except FileNotFoundError:
    channels = {}
    whitelist = {}

@client.event
async def on_ready():
    global uid
    print('We have logged in as {0.user}'.format(client))
    uid = client.user.id
    activity = discord.Activity(name='silence | after whitelist blacklist', type=discord.ActivityType.listening)
    await client.change_presence(activity=activity)


@client.event
async def on_message(message):
    nick = message.channel.guild.get_member(uid).display_name
    print(nick)

    if message.content.startswith(nick):
        command = message.content[len(nick):].split()
        if command[0] == 'after':
            time = sum(hr.Time(o).seconds for o in command[1:])
            channels[message.channel.id] = time
            await message.delete()
        if command[0] == 'delete':
            await message.delete()

    print(channels)
    print(message.channel.id)
    if message.channel.id in channels:
        print('test')
        await asyncio.sleep(channels[message.channel.id])
        await message.delete()

with open('token.txt') as f:
    client.run(f.read())
