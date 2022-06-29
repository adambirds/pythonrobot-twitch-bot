import random
from datetime import datetime, timezone

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

    @commands.command()
    async def gitcheatsheet(self, ctx: commands.Context) -> None:
        """
        !gitcheatsheet command
        """
        await ctx.send(
            "Here is an awesome git cheat sheet: https://education.github.com/git-cheat-sheet-education.pdf"
        )

    @commands.command()
    async def formatpy(self, ctx: commands.Context) -> None:
        """
        !formatpy command
        """
        await ctx.send(
            'The command to format Python files in your directory with black is "python -m black ." or "black ."'
        )

    @commands.command()
    async def uptime(self, ctx: commands.Context) -> None:
        """
        !uptime command
        """
        stream = await ctx.bot.fetch_streams(user_logins=[ctx.channel.name])
        if not stream:
            return await ctx.send("This channel is not currently live.")
        else:
            started_at = stream[0].started_at.replace(tzinfo=timezone.utc)
            uptime = datetime.utcnow().replace(tzinfo=timezone.utc) - started_at
            total_seconds = uptime.total_seconds()
            days, remainder = divmod(total_seconds, 86400)
            hours, remainder = divmod(remainder, 3600)
            minutes, seconds = divmod(remainder, 60)

            if days != 0:
                days_text = f"{int(days)} days, "
            elif days == 1:
                hours_text = f"{int(days)} day, "
            else:
                days_text = ""

            if hours != 0:
                hours_text = f"{int(hours)} hours, "
            elif hours == 1:
                hours_text = f"{int(hours)} hour, "
            else:
                hours_text = ""

            return await ctx.send(
                f"{ctx.channel.name} has been streaming for {days_text }{hours_text}{int(minutes)} minutes and {int(seconds)} seconds."
            )

    @commands.command(aliases=["pyenv", "venv", "virtualenv"])
    async def pyvenv(self, ctx: commands.Context) -> None:
        """
        !pyvenv (!pyenv, !venv, !virtualenv) command
        """
        await ctx.send(
            'The command to create a virtual environment in Python is "python -m venv venv".'
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

    @commands.command()
    async def project(self, ctx: commands.Context) -> None:
        """
        !project command
        """
        print(ctx.channel.name)
        if self.bot.conf_options[ctx.channel.name]["PROJECT"] != "":
            await ctx.send(f'{self.bot.conf_options[ctx.channel.name]["PROJECT"]}')
        else:
            return

    @commands.command(aliases=["calc"])
    async def calculator(
        self, ctx: commands.Context, value1: str = "", operator: str = "", value2: str = ""
    ) -> None:
        """
        !calculator command
        """
        try:
            value1_int = float(value1)
            value2_int = float(value2)
        except:
            return await ctx.send(
                f"@{ctx.author.name} you submitted an invalid number for your calculation."
            )

        match operator:
            case "+":
                answer = value1_int + value2_int
            case "-":
                answer = value1_int - value2_int
            case "*":
                answer = value1_int * value2_int
            case "/":
                try:
                    answer = value1_int / value2_int
                except:
                    return await ctx.send(f"@{ctx.author.name} you can't divide by 0.")

            case _:
                return await ctx.send(f"@{ctx.author.name} you submitted an invalid operator.")

        await ctx.send(f"@{ctx.author.name} the answer is {answer}.")


def prepare(bot: commands.Bot) -> None:
    bot.add_cog(CommandsCog(bot))
