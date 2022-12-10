# Autocomplete Me

This is a simple autocomplete for cities and wiktionary words.

## Commands

| Name              | Syntax                           |
| ----------------- | -------------------------------- |
| autocomplete city | `/autocomplete city city:[city]` |
| autocomplete word | `/autocomplete word word:[word]` |

## How to Use

### Running on the Cloud

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/x_i4mX?referralCode=t96gPh)

- Create an account
- Go to the [Discord Developer Portal](https://discord.com/developers/applications) and sign in
- Create a new application.
- Then go to the Bot tab and click "Add Bot".
- Reset the token and paste it in the `config.json` file.
- Go to the OAuth2 tab and select the "bot" scope.
- Copy the link and paste it in your browser.
- Invite the bot to your server.
- Run the bot by typing `python3 main.py` in the terminal.
- Enjoy!

### Running Locally:

```bash
git clone https://github.com/JustaSqu1d/autocomplete-me.git
cd autocomplete-me
pip3 install -r requirements.txt
```

- Go to the [Discord Developer Portal](https://discord.com/developers/applications) and sign in
- Create a new application.
- Then go to the Bot tab and click "Add Bot".
- Reset the token and paste it in the `config.json` file.
- Go to the OAuth2 tab and select the "bot" scope.
- Copy the link and paste it in your browser.
- Invite the bot to your server.
- Run the bot by typing `python3 main.py` in the terminal.
- Enjoy!

## Extra Notes

- Because of a Discord limitation, the bot can only display 25 results at a time.
