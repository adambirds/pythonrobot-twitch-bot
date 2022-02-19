import twitchio
from twitchio.ext import commands


class ModCommandsCog(commands.Cog):
    def __init__(self, bot: commands.Cog) -> None:
        self.bot = bot

    async def cog_check(self, ctx: commands.Context) -> bool:
        return ctx.author.is_mod

    @commands.command(aliases=["so"])
    async def shoutout(self, ctx: commands.Context, user: twitchio.User) -> None:
        """
        !shoutout (!so) command
        """

        await ctx.send(f"Check out @{user.display_name} over at twitch.tv/{user.name}")


def prepare(bot: commands.Bot) -> None:
    bot.add_cog(ModCommandsCog(bot))
