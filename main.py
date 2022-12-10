import json
import os
from urllib import parse

import discord

from utils.autocomplete import city_searcher, wiktionary_searcher

bot = discord.Bot()


@bot.event
async def on_ready():
    print("I am online!")

autocomplete_group = bot.create_group(
    name="autocomplete", invoke_without_command=True)


@autocomplete_group.command(
    name="wiktionary",
    description="Searches the Wiktionary for a word",
)
@discord.option(
    name="word",
    description="The word to search for",
    required=True,
    autocomplete=wiktionary_searcher
)
async def autocomplete_wiktionary(ctx, word: str):
    param = parse.urlencode({"q": word})
    await ctx.respond(
        f"Results about `{word}` on the internet.",
        view=discord.ui.View(
            discord.ui.Button(
                label="Google", url=f"https://www.google.com/search?{param}"
            ),
            discord.ui.Button(
                label="Bing", url=f"https://www.bing.com/search?{param}"
            ),
            discord.ui.Button(
                label="DuckDuckGo", url=f"https://www.duckduckgo.com/?{param}"
            ),
        ),
    )


@autocomplete_group.command(
    name="city",
    description="Searches for a city",
)
@discord.option(
    name="city",
    description="The city to search for",
    required=True,
    autocomplete=city_searcher
)
async def autocomplete_city(ctx, city: str):
    param = parse.urlencode({"q": city})
    await ctx.respond(
        f"Results about `{city}` on the internet.",
        view=discord.ui.View(
            discord.ui.Button(
                label="Google", url=f"https://www.google.com/search?{param}"
            ),
            discord.ui.Button(
                label="Bing", url=f"https://www.bing.com/search?{param}"
            ),
            discord.ui.Button(
                label="DuckDuckGo", url=f"https://www.duckduckgo.com/?{param}"
            ),
        ),
    )

try:
    TOKEN = os.environ.get("TOKEN")

except:
    with open("config.json") as f:
        config = json.load(f)
        TOKEN = config["token"]

bot.run(TOKEN)
