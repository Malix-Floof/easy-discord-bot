from os import getenv

import disnake
from disnake.ext import commands
from dotenv import load_dotenv


class EasyDiscordBot(commands.Bot):
    def __init__(self):
        super().__init__(
    	    command_prefix=getenv("COMMAND_PREFIX"),
    	    intents=disnake.Intents.all(),
        )

    async def on_ready(self):
        print("Запущен!")

load_dotenv()

bot = EasyDiscordBot()
bot.run(getenv("DISCORD_TOKEN"))
