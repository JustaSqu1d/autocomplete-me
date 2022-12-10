import discord
from utils.modals import City, Word

__all__ = (
    "city_searcher",
    "wiktionary_searcher",
)

cities = []
words = []

with open("utils/cities.txt") as f:
    RAW_CITIES = f.read().splitlines()

for i in RAW_CITIES:
    try:
        if i.count(",") > 1:  # this handles for cities with states/providences
            name = i.split(",")[0].split("\t")[1]
            search_count = i.split(",")[0].split("\t")[0].replace(" ", "")
            state = i.split(", ")[1]
            country = i.split(", ")[2]
            cities.append(City(
                name=name,
                search_count=search_count,
                state=state,
                country=country
            ))
        else:
            name = i.split(",")[0].split("\t")[1]
            search_count = i.split(",")[0].split("\t")[0].replace(" ", "")
            country = i.split(", ")[1]
            cities.append(City(
                name=name,
                search_count=search_count,
                country=country
            ))
    except IndexError:
        # this handles for the first line of the file
        pass

with open("utils/wiktionary.txt") as f:
    RAW_WORDS = f.read().splitlines()

for i in RAW_WORDS:
    if len(i.split()) > 1:
        words.append(Word(
            word=i.split()[1].lower(), search_count=i.split()[0]
        )
        )


async def city_searcher(ctx: discord.AutocompleteContext):
    if ctx.value == "":
        return ["Welcome to the City Autocomplete!"]

    queried_cities = []

    index = 1

    for city in cities:  # already sorted

        if (city.name.lower().startswith(ctx.value.lower(
        )) or city.state.lower().startswith(ctx.value.lower()) or city.country.lower().startswith(ctx.value.lower())):
            queried_cities.append(str(city))

            if index == 25:  # Discord limits the amount of autocomplete options to 25
                break
            else:
                index += 1

    return queried_cities


async def wiktionary_searcher(ctx: discord.AutocompleteContext):

    if ctx.value == "":
        return ["Welcome to the Wiktionary Autocomplete!"]

    queried_words = []

    index = 1

    for word in queried_words:  # already sorted
        if word.word.lower().startswith(ctx.value.lower()):
            queried_words.append(str(word))
            if index == 25:
                break
            else:
                index += 1

    return queried_words
