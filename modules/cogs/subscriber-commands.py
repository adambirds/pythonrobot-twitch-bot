from twitchio.ext import commands


class SubscriberCommandsCog(commands.Cog):
    def __init__(self, bot: commands.Cog) -> None:
        self.bot = bot

    async def cog_check(self, ctx: commands.Context) -> bool:
        return ctx.author.is_subscriber


def prepare(bot: commands.Bot) -> None:
    bot.add_cog(SubscriberCommandsCog(bot))
