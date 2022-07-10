from asyncio import events
import discord
import sys
from search import search
from discord.ext import tasks


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # an attribute we can access from our task
        self.counter = 0

    async def setup_hook(self) -> None:
        # start the task to run in the background
        self.my_background_task.start()
        
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')
        self.my_background_task.start()
        print('background task started')

    @tasks.loop(seconds=60)  # task runs every 60 seconds
    async def my_background_task(self):
        channel = self.get_channel('channel id') 
        print(channel) # channel ID goes here
        link = 'github release page'
        Henry = search()
        l1 = Henry.main(link)
        if l1 != None:
            file = open(l1, 'r')
            lines = file.read()
            print(lines)
            await channel.send(lines)

    @my_background_task.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()  # wait until the bot logs in
    



client = MyClient(intents=discord.Intents.default())      
client.run(sys.argv[1]) 

