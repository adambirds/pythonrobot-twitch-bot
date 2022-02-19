import twitchio
from twitchio.ext import commands


class EventsCog(commands.Cog):
    def __init__(self, bot: commands.Cog) -> None:
        self.bot = bot

    @commands.Cog.event()
    async def event_ready(self) -> None:
        """
        Ptints who the bot is logged in as when ready.
        """
        print(f"Logged in as | {self.bot.nick}")

    @commands.Cog.event()
    async def event_message(self, message: twitchio.Message) -> None:
        """
        Ignore messages sent by the bot and handle the commands.
        """
        if message.echo:
            return

        print(message.content)


def prepare(bot: commands.Bot) -> None:
    bot.add_cog(EventsCog(bot))
