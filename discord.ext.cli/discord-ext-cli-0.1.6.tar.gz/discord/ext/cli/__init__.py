import discord, asyncio, aiohttp
from discord.ext import commands
from aioconsole import aprint, ainput

__version__ = "0.1.6"

class CLI(commands.Bot):
    def __init__(self, channel_id : int, author_id : int = None, **kwargs):
        super().__init__(**kwargs)
        self.channel_id = channel_id
        self.author_id = author_id
        self.cli_start = False
        
    async def on_message(self, message):
        try:
            if self.cli_start is True:
                if message.channel.id == self.channel_id:
                    if message.author == self.user:
                        return
                    if self.author_id is not None:
                        if message.author.id == self.author_id:
                            await aprint(f"> {message.author} - {message.content}")
                            send_message = await ainput("[ Admin ] Send a message: ")
                            await message.channel.send(send_message)
                    else:
                        await aprint(f"> {message.author} - {message.content}")
                        send_message = await ainput("[ Admin ] Send a message: ")
                        await message.channel.send(send_message)
        except Exception:
            pass                                         
                    
        await self.process_commands(message)
                
        
    async def start_cli(self):
        cli = await ainput("Do you want to start the cli? [y | n] (n): ")
        cli = cli.lower()
        if cli == "y":
            self.cli_start = True
        elif cli == "n":
            self.cli_start = False
        else:
            await aprint(f"Invalid Option: {cli}")     
       
    def run(self, token : str):
        asyncio.get_event_loop().run_until_complete(self.start_cli())
        super().run(token)                   

class ShardedCLI(CLI, commands.AutoShardedBot):
    pass                  