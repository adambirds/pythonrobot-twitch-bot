# Import libraries
import random
import sys
from datetime import datetime
from typing import Any, List
from urllib.error import HTTPError

import pytz
import requests
import twitchio
import yaml
from aiohttp.web_runner import GracefulExit
from twitchio.ext import commands, eventsub


# Define function to process yaml config file
def process_config_file() -> Any:
    with open("config.yaml", "r") as stream:
        config_options = yaml.safe_load(stream)

    return config_options


# Define checks class.
class Checks:
    def is_mod(self, ctx: commands.Context) -> bool:
        return ctx.message.author.is_mod == 1


# Define Bot class
class Bot(commands.Bot):
    QUOTES_API = "https://api.quotable.io/random"

    def __init__(self, access_token: str, prefix: str, initial_channels: List[str]):
        """
        Tells the Bot class which token it should use, channels to connect to and prefix to use.
        """
        super().__init__(token=access_token, prefix=prefix, initial_channels=initial_channels)

    async def event_ready(self) -> None:
        """
        Ptints who the bot is logged in as when ready.
        """
        print(f"Logged in as | {self.nick}")

    async def event_message(self, message: twitchio.Message) -> None:
        """
        Ignore messages sent by the bot and handle the commands.
        """
        if message.echo:
            return

        print(message.content)

        await self.handle_commands(message)

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
        if conf_options[ctx.channel.name]["SOCIALS"]["GITHUB"] != "":
            await ctx.send(
                f'Here is my GitHub link: {conf_options[ctx.channel.name]["SOCIALS"]["GITHUB"]}'
            )
        else:
            await ctx.send("I don't currently have a GitHub account.")

    @commands.command()
    async def discord(self, ctx: commands.Context) -> None:
        """
        !discord command
        """
        if conf_options[ctx.channel.name]["SOCIALS"]["DISCORD"] != "":
            await ctx.send(
                f'Here is the link to my Discord server: {conf_options[ctx.channel.name]["SOCIALS"]["DISCORD"]}'
            )
        else:
            await ctx.send("I don't currently have a Discord server.")

    @commands.command()
    async def youtube(self, ctx: commands.Context) -> None:
        """
        !youtube command
        """
        if conf_options[ctx.channel.name]["SOCIALS"]["YOUTUBE"] != "":
            await ctx.send(
                f'Here is the link to my YouTube channel: {conf_options[ctx.channel.name]["SOCIALS"]["YOUTUBE"]}'
            )
        else:
            await ctx.send("I don't currently have a YouTube channel.")

    @commands.command(aliases=["ig", "insta"])
    async def instagram(self, ctx: commands.Context) -> None:
        """
        !instagram command
        """
        if conf_options[ctx.channel.name]["SOCIALS"]["INSTAGRAM"] != "":
            await ctx.send(
                f'Here is the link to my Instagram page: {conf_options[ctx.channel.name]["SOCIALS"]["INSTAGRAM"]}'
            )
        else:
            await ctx.send("I don't currently have an Instagram page.")

    @commands.command()
    async def twitter(self, ctx: commands.Context) -> None:
        """
        !twitter command
        """
        if conf_options[ctx.channel.name]["SOCIALS"]["TWITTER"] != "":
            await ctx.send(
                f'Here is the link to my Twitter page: {conf_options[ctx.channel.name]["SOCIALS"]["TWITTER"]}'
            )
        else:
            await ctx.send("I don't currently have a Twitter page.")

    @commands.command(aliases=["fb"])
    async def facebook(self, ctx: commands.Context) -> None:
        """
        !facebook command
        """
        if conf_options[ctx.channel.name]["SOCIALS"]["FACEBOOK"] != "":
            await ctx.send(
                f'Here is the link to my Facebook page: {conf_options[ctx.channel.name]["SOCIALS"]["FACEBOOK"]}'
            )
        else:
            await ctx.send("I don't currently have a Facebook page.")

    @commands.command()
    async def reddit(self, ctx: commands.Context) -> None:
        """
        !reddit command
        """
        if conf_options[ctx.channel.name]["SOCIALS"]["REDDIT"] != "":
            await ctx.send(
                f'Here is the link to my Reddit: {conf_options[ctx.channel.name]["SOCIALS"]["REDDIT"]}'
            )
        else:
            await ctx.send("I don't currently have a Reddit.")

    @commands.command()
    async def website(self, ctx: commands.Context) -> None:
        """
        !website command
        """
        if conf_options[ctx.channel.name]["SOCIALS"]["WEBSITE"] != "":
            await ctx.send(
                f'Here is the link to my website: {conf_options[ctx.channel.name]["SOCIALS"]["WEBSITE"]}'
            )
        else:
            await ctx.send("I don't currently have a website.")

    @commands.command(aliases="links")
    async def socials(self, ctx: commands.Context) -> None:
        """
        !socials command
        """
        social: str
        social_text = ""
        for social in conf_options[ctx.channel.name]["SOCIALS"]:
            if conf_options[ctx.channel.name]["SOCIALS"][social] != "":
                print(social.capitalize())
                social_text += social.capitalize()
                social_text += ":"
                social_text += " "
                social_text += conf_options[ctx.channel.name]["SOCIALS"][social]
                social_text += " "
                social_text += "-"
                social_text += " "

        await ctx.send(social_text.rstrip(" - "))

    @commands.command(aliases=["so"])
    async def shoutout(self, ctx: commands.Context, user: twitchio.User) -> None:
        """
        !shoutout (!so) command
        """
        if not Checks.is_mod(self, ctx):
            return

        await ctx.send(f"Check out @{user.display_name} over at twitch.tv/{user.name}")

    @commands.command(aliases=["roll"])
    async def dice(self, ctx: commands.Context) -> None:
        """
        !dice (!roll) command
        """
        await ctx.send(f"You rolled a {random.randint(1,6)}")

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
            f'Do you want this bot on your channel? If so check out its GitHub: {conf_options["APP"]["BOT_GITHUB_LINK"]}'
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
            f"You can the list of commands which this bot supports here: {conf_options['APP']['BOT_COMMANDS_LINK']}."
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


if __name__ == "__main__":
    conf_options = process_config_file()
    channel_names = []
    for channel in conf_options["APP"]["ACCOUNTS"]:
        channel_names.append("#" + channel["name"])
    bot = Bot(
        access_token=conf_options["APP"]["ACCESS_TOKEN"],
        prefix="!",
        initial_channels=channel_names,
    )
    eventsubbot = Bot.from_client_credentials(
        client_id=conf_options["APP"]["CLIENT_ID"],
        client_secret=conf_options["APP"]["CLIENT_SECRET"],
    )

    @eventsubbot.event()
    async def event_eventsub_notification_follow(payload: eventsub.ChannelFollowData) -> None:
        """
        Reacts to receicing a new channel follow event. It will respond in chat thanking the follower and giving them the discord link.
        """
        print(f"{payload.data.user.name} followed {payload.data.broadcaster.name}")
        channel = bot.get_channel(payload.data.broadcaster.name)
        if conf_options[(payload.data.broadcaster.name).lower()]["SOCIALS"]["DISCORD"] != "":
            await channel.send(
                f'Thanks for the follow @{payload.data.user.name}! Please join our discord server: {conf_options[(payload.data.broadcaster.name).lower()]["SOCIALS"]["DISCORD"]}'
            )
        else:
            await channel.send(f"Thanks for the follow {payload.data.user.name}!")

    @eventsubbot.event()
    async def event_eventsub_notification_stream_start(
        payload: eventsub.StreamOnlineData,
    ) -> None:
        """
        Reacts to receiving a stream start event.
        """
        print(payload.data.id)

    @eventsubbot.event()
    async def event_eventsub_notification_channel_raid(
        payload: eventsub.ChannelRaidData,
    ) -> None:
        """
        Reacts to receiving a channel raid event.
        """
        channel = bot.get_channel(payload.receiver.name)
        await channel.send(
            f"Thanks for the raid @{payload.raider.display_name} who has just brought with them {payload.viewer_count} viewers."
        )

    eventsub_client = eventsub.EventSubClient(
        eventsubbot,
        conf_options["APP"]["SECRET_STRING"],
        conf_options["APP"]["CALLBACK_URL"],
    )

    async def subscribe_follows(channel_id: int) -> None:
        """
        Subscribes to new channel follow events.
        """
        try:
            await eventsub_client.subscribe_channel_follows(channel_id)
        except twitchio.HTTPException:
            pass

    async def subscribe_stream_starts(channel_id: int) -> None:
        """
        Subscribes to stream start events.
        """
        try:
            await eventsub_client.subscribe_channel_stream_start(channel_id)
        except twitchio.HTTPException:
            pass

    async def subscribe_channel_raid(channel_id: int) -> None:
        """
        Subscribes to channel raid events.
        """
        try:
            await eventsub_client.subscribe_channel_raid(channel_id)
        except twitchio.HTTPException:
            pass

    bot.loop.create_task(eventsub_client.listen(port=conf_options["APP"]["PORT"]))
    bot.loop.create_task(bot.connect())
    for channel in conf_options["APP"]["ACCOUNTS"]:
        eventsubbot.loop.create_task(subscribe_follows(channel["id"]))
        eventsubbot.loop.create_task(subscribe_stream_starts(channel["id"]))
        eventsubbot.loop.create_task(subscribe_channel_raid(channel["id"]))
    try:
        bot.loop.run_forever()
    except GracefulExit:
        sys.exit(0)
