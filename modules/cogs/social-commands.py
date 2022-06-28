from twitchio.ext import commands


class SocialCommandsCog(commands.Cog):
    def __init__(self, bot: commands.Cog) -> None:
        self.bot = bot

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
            return

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
            return

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
            return

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
            return

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
            return

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
            return

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
            return

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
            return

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
            return

    @commands.command()
    async def patreon(self, ctx: commands.Context) -> None:
        """
        !patron command
        """
        if self.bot.conf_options[ctx.channel.name]["SOCIALS"]["PATREON"] != "":
            await ctx.send(
                f'Here is the link to my patreon: {self.bot.conf_options[ctx.channel.name]["SOCIALS"]["PATREON"]}'
            )
        else:
            return

    @commands.command(aliases="links")
    async def socials(self, ctx: commands.Context) -> None:
        """
        !socials command
        """
        social: str
        social_text = ""
        socials = self.bot.conf_options[ctx.channel.name]["SOCIALS"]
        socials = {k: socials[k] for k in sorted(socials)}
        for social in socials:
            if socials[social] != "":
                print(social.capitalize())
                social_text += f"{social.capitalize()}: {socials[social]} - "
        if social_text != "":
            await ctx.send(social_text.rstrip(" - "))
        else:
            return


def prepare(bot: commands.Bot) -> None:
    bot.add_cog(SocialCommandsCog(bot))
