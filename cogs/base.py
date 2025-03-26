from disnake.ext import commands


class CogExample(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def hello(self, inter):
	      await inter.response.send_message(f"Привет, {inter.author.mention}!") # отправит в чат Привет, @user!


def setup(bot):
    bot.add_cog(CogExample(bot))
