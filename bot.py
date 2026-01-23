import disnake
from disnake.ext import commands
from config import settings


bot = commands.Bot(
	command_prefix = settings['PREFIX'], 
	intents = disnake.Intents.all()
)

@bot.event
async def on_ready(self):
    print("Запущен!")

bot = EasyDiscordBot()
bot.load_extensions("cogs")
bot.run(settings['TOKEN'])
