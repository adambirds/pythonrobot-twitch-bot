import random
from datetime import datetime
from urllib.error import HTTPError

import pytz
import requests
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

    @commands.command()
    async def github(self, ctx: commands.Context) -> None:
        """
        !github command
        """
        print(ctx.channel.name)
        if self.bot.conf_options[ctx.channel.name]["SOCIALS"]["GITHUB"] != "":
            await ctx.send(
                f'Here is my GitHub link: {self.bot.conf_options[ctx.channel.name]["SOCIALS"]["GITHUB"]}'
            )
        else:
            await ctx.send("I don't currently have a GitHub account.")

    @commands.command()
    async def discord(self, ctx: commands.Context) -> None:
        """
        !discord command
        """
        if self.bot.conf_options[ctx.channel.name]["SOCIALS"]["DISCORD"] != "":
            await ctx.send(
                f'Here is the link to my Discord server: {self.bot.conf_options[ctx.channel.name]["SOCIALS"]["DISCORD"]}'
            )
        else:
            await ctx.send("I don't currently have a Discord server.")

    @commands.command()
    async def youtube(self, ctx: commands.Context) -> None:
        """
        !youtube command
        """
        if self.bot.conf_options[ctx.channel.name]["SOCIALS"]["YOUTUBE"] != "":
            await ctx.send(
                f'Here is the link to my YouTube channel: {self.bot.conf_options[ctx.channel.name]["SOCIALS"]["YOUTUBE"]}'
            )
        else:
            await ctx.send("I don't currently have a YouTube channel.")

    @commands.command(aliases=["ig", "insta"])
    async def instagram(self, ctx: commands.Context) -> None:
        """
        !instagram command
        """
        if self.bot.conf_options[ctx.channel.name]["SOCIALS"]["INSTAGRAM"] != "":
            await ctx.send(
                f'Here is the link to my Instagram page: {self.bot.conf_options[ctx.channel.name]["SOCIALS"]["INSTAGRAM"]}'
            )
        else:
            await ctx.send("I don't currently have an Instagram page.")

    @commands.command()
    async def twitter(self, ctx: commands.Context) -> None:
        """
        !twitter command
        """
        if self.bot.conf_options[ctx.channel.name]["SOCIALS"]["TWITTER"] != "":
            await ctx.send(
                f'Here is the link to my Twitter page: {self.bot.conf_options[ctx.channel.name]["SOCIALS"]["TWITTER"]}'
            )
        else:
            await ctx.send("I don't currently have a Twitter page.")

    @commands.command(aliases=["fb"])
    async def facebook(self, ctx: commands.Context) -> None:
        """
        !facebook command
        """
        if self.bot.conf_options[ctx.channel.name]["SOCIALS"]["FACEBOOK"] != "":
            await ctx.send(
                f'Here is the link to my Facebook page: {self.bot.conf_options[ctx.channel.name]["SOCIALS"]["FACEBOOK"]}'
            )
        else:
            await ctx.send("I don't currently have a Facebook page.")

    @commands.command()
    async def reddit(self, ctx: commands.Context) -> None:
        """
        !reddit command
        """
        if self.bot.conf_options[ctx.channel.name]["SOCIALS"]["REDDIT"] != "":
            await ctx.send(
                f'Here is the link to my Reddit: {self.bot.conf_options[ctx.channel.name]["SOCIALS"]["REDDIT"]}'
            )
        else:
            await ctx.send("I don't currently have a Reddit.")

    @commands.command()
    async def website(self, ctx: commands.Context) -> None:
        """
        !website command
        """
        if self.bot.conf_options[ctx.channel.name]["SOCIALS"]["WEBSITE"] != "":
            await ctx.send(
                f'Here is the link to my website: {self.bot.conf_options[ctx.channel.name]["SOCIALS"]["WEBSITE"]}'
            )
        else:
            await ctx.send("I don't currently have a website.")

    @commands.command()
    async def tiktok(self, ctx: commands.Context) -> None:
        """
        !tiktok command
        """
        if self.bot.conf_options[ctx.channel.name]["SOCIALS"]["TIKTOK"] != "":
            await ctx.send(
                f'Here is the link to my tiktok: {self.bot.conf_options[ctx.channel.name]["SOCIALS"]["TIKTOK"]}'
            )
        else:
            await ctx.send("I don't currently have tiktok.")

    @commands.command(aliases="links")
    async def socials(self, ctx: commands.Context) -> None:
        """
        !socials command
        """
        social: str
        social_text = ""
        for social in self.bot.conf_options[ctx.channel.name]["SOCIALS"]:
            if self.bot.conf_options[ctx.channel.name]["SOCIALS"][social] != "":
                print(social.capitalize())
                social_text += f'{social.capitalize()}: {self.bot.conf_options[ctx.channel.name]["SOCIALS"][social]} - '

        await ctx.send(social_text.rstrip(" - "))

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
        timezone = timezone.replace(" ", "_")
        if timezone in pytz.all_timezones:
            date_time = datetime.now(pytz.timezone(timezone)).strftime("%A %-dth %B %Y %H:%M")
            await ctx.send(f"The date and time in {timezone} is {date_time}.")
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
        try:
            response = requests.get(self.QUOTES_API)
            response.raise_for_status()
        except HTTPError:
            return
        except Exception:
            return

        payload = response.json()
        await ctx.send(f"{payload['author']}: \"{payload['content']}\"")

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
            "Here is an awesome Python cheat sheet: https://learnxinyminutes.com/docs/python/."
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
