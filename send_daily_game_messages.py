import discord
import os
from discord.ext import tasks
from discord.ext import commands
import time

#class MyClient(discord.Client):
class MyClient(commands.Bot):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

  async def on_ready(self):
    print('We have logged in as {0.user}'.format(client))
    self.SendMessageToRpgBot.start()
    time.sleep(10)
    self.SendMessageToMee6Bot.start()
    time.sleep(10)
    self.SendMessageToFortniteBot.start()
    time.sleep(10)

  @tasks.loop(minutes=1)
  async def SendMessageToRpgBot(self):
    channel = self.get_channel(int(os.environ['RPG_Channel_ID']))
    
    message = await channel.send("rpg daily")
    await self.process_commands(message)
    time.sleep(5)
    message = await channel.send("rpg weekly")
    await self.process_commands(message)
    time.sleep(5)

  @tasks.loop(minutes=1)
  async def SendMessageToMee6Bot(self):
    channel = self.get_channel(int(os.environ['MEE6_Game_Channel_ID']))
    message = await channel.send("/daily")
    await self.process_commands(message)
    time.sleep(5)
    message = await channel.send("/weekly")
    await self.process_commands(message)
    time.sleep(5)
  
  @tasks.loop(minutes=1)
  async def SendMessageToFortniteBot(self):
    channel = self.get_channel(int(os.environ['Fortnite_Game_Channel_ID']))
    message = await channel.send("/claim-daily")
    await self.process_commands(message)
    time.sleep(10)
    message = await channel.send("/research collect")
    await self.process_commands(message)
    time.sleep(10)

  @SendMessageToRpgBot.before_loop
  @SendMessageToMee6Bot.before_loop
  @SendMessageToFortniteBot.before_loop
  async def before_my_task(self):
      await self.wait_until_ready() # wait until the bot logs in

if __name__ == "__main__":
  intents = discord.Intents.default()
  client = MyClient(intents = intents, command_prefix="!")

  # To run using bot token
  #client.run(os.environ['TOKEN'])

  # To run using user token
  client.run(os.environ['My_Token'], bot=False)