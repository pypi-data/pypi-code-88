import discord
import aiofiles
import asyncio

from textwrap import dedent


intents = discord.Intents.default()
intents.members = True



class DocGen:
    def __init__(self, bot):
        self.bot = bot

    async def generate_docs(self,  command) -> None:
        async with aiofiles.open("docs.md", "a") as file:
            await file.write(dedent(f"""
                **Command Name: {command.name}**
                **Command Description: {command.help}
                <br>
                <br>
                """))

    def document_code(self):
        def wrapper(func):
            asyncio.run(self.generate_docs(func))

        return wrapper
