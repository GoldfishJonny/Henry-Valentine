import discord
import sys
import search
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

Henry = search.search('https://github.com/GoldfishJonny/Henry-Valentine')
print(Henry)
client.run(sys.argv[1]) 