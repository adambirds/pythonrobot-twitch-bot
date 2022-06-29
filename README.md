# PythonRobot TwitchBot
[![code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![mypy coverage](https://img.shields.io/badge/mypy-100%25-green.svg)](https://github.com/python/mypy)
![GitHub Sponsors](https://img.shields.io/github/sponsors/adambirds)

Developed for the channels of [PythonPhil](https://twitch.tv/pythonphil) and [CodingAndGamingWithAdam](https://twitch.tv/codingandgamingwithadam).

## Support
For support using this bot, please join our [official support server](https://discord.gg/f5veJaa4ZX) on [Discord](https://discord.com).

[![discord](https://img.shields.io/discord/941885906443468880?color=%237289DA&label=Coding%20With%20Adam&logo=discord&logoColor=white)](https://discord.gg/f5veJaa4ZX)

## Source
The source code can be found [here](https://github.com/adambirds/pythonrobot-twitch-bot).

Contributions welcome and gratefully appreciated!

## Requirements
Python 3 (Version 3.6 or later).

## Installation

This has only been tested on Linux, so preferably use Linux or WSL 2 if on Windows.

Navigate to where you will store the bot files, then run:

```
git clone git@github.com:adambirds/pythonrobot-twitch-bot.git
```

Then run:

```
tools/setup/prep-prod-environment
```

Then run:

```
cp example-config.yaml config.yaml
```

You will then need to edit config.yaml to your needs. You shouldn't delete any of the keys, however any of the keys under `SOCIALS` can be set to `""` which will inform the bot that you don't have an account.

The `ACCESS_TOKEN` key can be generated using this [generator](https://twitchtokengenerator.com).

The `CLIENT_ID` and `CLIENT_SECRET` keys have to be got from creating and registering your own application at [dev.twitch.tv](https://dev.twitch.tv).

The `SECRET_STRING` key can be set to any string you like but this cannot be changed without a lot of difficulty down the line for you. For security we highly reccommend that this is set to something long, ideally a randomly generated string of characters.

The `CALLBACK_URL` key should be set to the domain you wish Twitch to send the webhooks to for which we will now setup a web server for.

The `PORT` key should be set to a port number that the internal web server that the bot creates will listen on. By default this is set to `4000` in the config file.

**Twitch** requires your callback URL to be accessible via `https://` with an `SSL` certificate on port `443`. The bot doesn't support this so we need set up a reverse proxy to handle this for us. For this I reccommend using **Nginx** which you can install with the below command:

```
apt-get install nginx
```

For your SSL certificate you can use any valid SSL as long as it isn't self-signed. For a free SSL certificate I reccomend that you use [Lets Encrypt](https://letsencrypt.org). You can find the instructions on how to generate your SSL [here](https://certbot.eff.org).

I have included an example nginx config file [here](https://github.com/adambirds/pythonrobot-twitch-bot/blob/main/example-nginx-virtualhost.conf). Once you have this running the only thing then left is to setup your bot to run as a service if you wish which you can do by amending the `./pythonrobot-twitch-bot.service` file with your working directorys and copying it using the following command:

```
cp ./pythonrobot-twitch-bot.service /lib/systemd/system/
```

Then run:

```
systemctl daemon-reload
```

Then run:

```
systemctl start pythonrobot-twitch-bot
```

And then to ensure it starts when your server does run:

```
systemctl enable pythonrobot-twitch-bot
```

## Commands and Events

### Commands

The bot supports the following commands:

| Command | Aliases | Example | Permissions | Purpose |
|-------- | ------- | ------- | ----------- | ------- |
| !8ball | | `!8ball Am I amazing?` | Everyone | The bot replies to a yes or no question. |
| !ban | | `!ban @adamistesting` or `!ban @adamistesting spamming channel`| Moderators | Ban user with or without a reason. |
| !dice | !roll | `!dice` | Everyone | Random number between 1 and 6. |
| !discord | | `!discord` | Everyone | The streamers discord link. |
| !facebook | !fb | `!facebook` | Everyone | The streamers facebook link. |
| !formatpy | | `!formatpy` | Everyone | Reminds someone how to format in python |
| !getthisbot | | `!getthisbot` | Everyone | The link to the bots github |
| !gitcheatsheet | | `!gitcheatsheet` | Everyone | The bot will reply with link to git cheat sheet. |
| !github | | `!github` | Everyone | The streamers github link. |
| !hello | | `!hello` | Everyone | The bot replies hello |
| !help | !commands | `!help` | Everyone | The bot replies with the link to these commands. |
| !instagram | !ig , !insta | `!instagram` | Everyone | The streamers instagram link. |
| !patreon | | `!patreon` | Everyone | The streamers patreon link. |
| !pycheatsheet | | `!pycheatsheet` | Everyone | The bot replies with the link to a Python cheat sheet. |
| !project | | `!project` | Everyone | The bot replies about information on the current project. |
| !pyvenv | !pyenv, !venv, !virtualenv | `!pyvenv` | Everyone | The bot replies with the command to create a Python virtual environment. |
| !quote | | `!quote` | Everyone | The bot replies with a random quote. |
| !reddit | | `!reddit` | Everyone | The streamers reddit link. |
| !shoutout | !so | `!shoutout pythonphil` | Moderators | Shoutout a fellow streamer |
| !socials | !links | `!socials` | Everyone | The streamers social mnedia links. |
| !tiktok | | `!tiktok` | Everyone | The streamers tiktok link. |
| !time | !date , !datetime | `!time Europe/London` | Everyone | Current time anywhere in world |
| !timeout | !to | `!timeout @adamistesting 10` or `!timeout @adamistesting 10 spamming channel` | Moderators | Timeout user for specified number of seconds with or without a reason. |
| !twitter | | `!twitter` | Everyone | The streamers twitter link. |
| !unban | | `!unban @adamistesting` | Moderators | Unban user. |
| !uptime | | `!uptime` | Everyone | Display how long the streamer has been streaming for. |
| !website | | `!website` | Everyone | The streamers website link. |
| !youtube | | `!youtube` | Everyone | The streamers youtube link. |

### Events
The bot also currently reacts to the following events:

- New Follower - The bot will thank the follower and if the stream has a discord, give them the link.
- Channel Raid - The bot will shoutout the raider, thank them, and announce how many views they brought with them.

## License

This project is released under the [GNU GENERAL PUBLIC LICENSE v3](https://github.com/adambirds/pythonrobot-twitch-bot/blob/main/LICENSE).

## Contributing

Anybody is welcome to contribute to this project. I just ask that you check out our contributing guidelines
[here](https://github.com/adambirds/pythonrobot-twitch-bot/blob/main/docs/contributing/contributing.md) first.
