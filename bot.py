# Import libraries
from twitchio.ext import commands, eventsub
import twitchio
import yaml
import random

# Define function to process yaml config file
def process_config_file():
    with open("config.yaml", "r") as stream:
        config_options = yaml.safe_load(stream)

    return config_options

# Define checks class.
class Checks():
    def is_owner(self, ctx):
        return str(ctx.message.author.id) == self.client.config["OWNER_ID"]

    def is_admin(self, ctx):
        return str(ctx.message.author.id) in self.client.config["ADMIN_IDS"]

    def is_mod(self, ctx):
        return ctx.message.author.is_mod == 1

# Define Bot class
class Bot(commands.Bot):
    def __init__(self, access_token, prefix, initial_channels):
        """
        Tells the Bot class which token it should use, channels to connect to and prefix to use.
        """
        super().__init__(
            token=access_token, prefix=prefix, initial_channels=initial_channels
        )

    async def event_ready(self):
        """
        Ptints who the bot is logged in as when ready.
        """
        print(f"Logged in as | {self.nick}")

    async def event_message(self, message):
        """
        Ignore messages sent by the bot and handle the commands.
        """
        if message.echo:
            return

        print(message.content)

        await self.handle_commands(message)

    @commands.command()
    async def hello(self, ctx: commands.Context):
        """
        !hello command
        """
        await ctx.send(f"Hello {ctx.author.display_name}!")

    @commands.command()
    async def github(self, ctx: commands.Context):
        """
        !github command
        """
        print(ctx.channel.name)
        if conf_options[ctx.channel.name]["GITHUB_LINK"] != "":
            await ctx.send(
                f'Here is my GitHub link: {conf_options[ctx.channel.name]["GITHUB_LINK"]}'
            )
        else:
            await ctx.send(f"I don't currently have a GitHub account.")

    @commands.command()
    async def discord(self, ctx: commands.Context):
        """
        !discord command
        """
        if conf_options[ctx.channel.name]["DISCORD_LINK"] != "":
            await ctx.send(
                f'Here is the link to my Discord server: {conf_options[ctx.channel.name]["DISCORD_LINK"]}'
            )
        else:
            await ctx.send(f"I don't currently have a Discord server.")
    
    @commands.command()
    async def youtube(self, ctx: commands.Context):
        """
        !youtube command
        """
        if conf_options[ctx.channel.name]["YOUTUBE_LINK"] != "":
            await ctx.send(
                f'Here is the link to my YouTube channel: {conf_options[ctx.channel.name]["YOUTUBE_LINK"]}'
            )
        else:
            await ctx.send(f"I don't currently have a YouTube channel.")
    
    @commands.command()
    async def instagram(self, ctx: commands.Context):
        """
        !instagram command
        """
        if conf_options[ctx.channel.name]["INSTAGRAM_LINK"] != "":
            await ctx.send(
                f'Here is the link to my Instagram page: {conf_options[ctx.channel.name]["INSTAGRAM_LINK"]}'
            )
        else:
            await ctx.send(f"I don't currently have an Instagram page.")
    
    @commands.command()
    async def twitter(self, ctx: commands.Context):
        """
        !twitter command
        """
        if conf_options[ctx.channel.name]["TWITTER_LINK"] != "":
            await ctx.send(
                f'Here is the link to my Twitter page: {conf_options[ctx.channel.name]["TWITTER_LINK"]}'
            )
        else:
            await ctx.send(f"I don't currently have a Twitter page.")
    
    @commands.command()
    async def facebook(self, ctx: commands.Context):
        """
        !facebook command
        """
        if conf_options[ctx.channel.name]["FACEBOOK_LINK"] != "":
            await ctx.send(
                f'Here is the link to my Facebook page: {conf_options[ctx.channel.name]["FACEBOOK_LINK"]}'
            )
        else:
            await ctx.send(f"I don't currently have a Facebook page.")
    
    @commands.command(aliases=['so'])
    async def shoutout(self, ctx: commands.Context, user: twitchio.User):
        """
        !shoutout (!so) command
        """
        if not Checks.is_mod(self, ctx):
            return
        
        await ctx.send(f"Check out @{user.display_name} over at twitch.tv/{user.name}")

    @commands.command(aliases=["roll"])
    async def dice(self, ctx: commands.Context):
        """
        !dice (!roll) command
        """
        await ctx.send(f"You rolled a {random.randint(1,6)}")


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
    async def event_eventsub_notification_follow(payload: eventsub.ChannelFollowData):
        """
        Reacts to receicing a new channel follow event. It will respond in chat thanking the follower and giving them the discord link.
        """
        print(f"{payload.data.user.name} followed {payload.data.broadcaster.name}")
        channel = bot.get_channel(payload.data.broadcaster.name)
        if conf_options[(payload.data.broadcaster.name).lower()]["DISCORD_LINK"] != "":
            await channel.send(
                f"Thanks for the follow {payload.data.user.name}! Please join our discord server: {conf_options[(payload.data.broadcaster.name).lower()]['DISCORD_LINK']}"
            )
        else:
            await channel.send(f"Thanks for the follow {payload.data.user.name}!")

    @eventsubbot.event()
    async def event_eventsub_notification_stream_start(
        payload: eventsub.StreamOnlineData,
    ):
        """
        Reacts to receiving a stream start event.
        """
        print(payload.data.id)

    eventsub_client = eventsub.EventSubClient(
        eventsubbot,
        conf_options["APP"]["SECRET_STRING"],
        conf_options["APP"]["CALLBACK_URL"],
    )

    async def subscribe_follows(channel_id):
        """
        Subscribes to new channel follow events.
        """
        try:
            await eventsub_client.subscribe_channel_follows(channel_id)
        except twitchio.HTTPException:
            pass

    async def subscribe_stream_starts(channel_id):
        """
        Subscribes to stream start events.
        """
        try:
            await eventsub_client.subscribe_channel_stream_start(channel_id)
        except twitchio.HTTPException:
            pass

    bot.loop.create_task(eventsub_client.listen(port=4000))
    bot.loop.create_task(bot.connect())
    for channel in conf_options["APP"]["ACCOUNTS"]:
        eventsubbot.loop.create_task(subscribe_follows(channel["id"]))
        eventsubbot.loop.create_task(subscribe_stream_starts(channel["id"]))
    bot.loop.run_forever()
