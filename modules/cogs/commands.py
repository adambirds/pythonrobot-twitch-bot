import random
from datetime import datetime

import pytz
from twitchio.ext import commands


class CommandsCog(commands.Cog):
    def __init__(self, bot: commands.Cog) -> None:
        self.bot = bot

    @commands.command()
    async def hello(self, ctx: commands.Context) -> None:
        """
        !hello command
        """
        await ctx.send(f"Hello {ctx.author.display_name}!")

    @commands.command(aliases=["roll"])
    async def dice(self, ctx: commands.Context) -> None:
        """
        !dice (!roll) command
        """
        await ctx.send(f"You rolled a {random.randint(1,6)}.")

    @commands.command(aliases=["date", "datetime"])
    async def time(self, ctx: commands.Context, *, timezone: str = "") -> None:
        """
        !time (!date) (!datetime) command
        """
        if timezone != "":
            timezone = timezone.replace(" ", "_")
            if timezone in pytz.all_timezones:
                date_time = datetime.now(pytz.timezone(timezone)).strftime("%A %-dth %B %Y %H:%M")
                await ctx.send(f"The date and time in {timezone} is {date_time}.")
            else:
                return
        else:
            timezone = self.bot.conf_options[ctx.channel.name]["TIMEZONE"]
            if timezone in pytz.all_timezones:
                date_time = datetime.now(pytz.timezone(timezone)).strftime("%A %-dth %B %Y %H:%M")
                await ctx.send(
                    f"The current date and time for the streamer in {timezone} is {date_time}."
                )
            else:
                return

    @commands.command()
    async def getthisbot(self, ctx: commands.Context) -> None:
        """
        !getthisbot command
        """
        await ctx.send(
            f'Do you want this bot on your channel? If so check out its GitHub: {self.bot.conf_options["APP"]["BOT_GITHUB_LINK"]}'
        )

    @commands.command()
    async def quote(self, ctx: commands.Context) -> None:
        """
        !quote command
        """
        async with self.bot.session.get(self.bot.QUOTES_API) as r:
            json_data = await r.json(content_type="application/json")
        await ctx.send(f"{json_data['author']}: \"{json_data['content']}\"")

    @commands.command(aliases=["commands"])
    async def help(self, ctx: commands.Context) -> None:
        """
        !help (!commands) command
        """
        await ctx.send(
            f"You can the list of commands which this bot supports here: {self.bot.conf_options['APP']['BOT_COMMANDS_LINK']}."
        )

    @commands.command()
    async def pycheatsheet(self, ctx: commands.Context) -> None:
        """
        !pycheatsheet command
        """
        await ctx.send(
            "Here are some awesome Python cheat sheets: Beginner: https://learnxinyminutes.com/docs/python/ More Advanced: https://gto76.github.io/python-cheatsheet/"
        )

    @commands.command(name="8ball")
    async def eight_ball(self, ctx: commands.Context, *, question: str = "") -> None:
        """
        !8ball command
        """
        POSSIBLE_ANSWERS = [
            "Of Course",
            "Yes",
            "No",
            "Of Course Not",
            "Definitely",
            "Definitely Not",
        ]
        if question != "":
            list_length = len(POSSIBLE_ANSWERS)
            answer = POSSIBLE_ANSWERS[random.randint(0, list_length - 1)]
            await ctx.send(f"Magic 8ball says: {answer}!")
        else:
            return


def prepare(bot: commands.Bot) -> None:
    bot.add_cog(CommandsCog(bot))
