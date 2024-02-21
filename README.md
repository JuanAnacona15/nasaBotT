# Telegram bot for NASA

This is a Telegram bot that uses the NASA API to get interesting information about space. The bot is built in Python and uses the `telebot` and `requests` libraries.

## Requirements
    - Python 3
    - Install the necessary libraries using the following commands:
        For telebot: pip install telebot.
        For requests: pip install requests.
    - Get the token of the bot in which you are going to use the ek script.
    - Get your API key at: https://api.nasa.gov

## Instructions to execute
    Once you have the requirements, do the following:
    1- In the credentials.py file edit line 3 changing "your_token" to your Telegram bot token.
    2- In the credentials.py file edit line 7 changing "your_apikey" to your NASA API api key.
    3- Finally, you can run the bot using the command >python nasaBot.py

## To run the bot
    Use the command: python bot_nasa.py

## Language
    Currently, the bot is in Spanish.

### Bot Commands
    - /start: Send a welcome message, what the bot is for and useful commands.
    - /help: Send a message explaining the bot's functionalities.
    - /imageNasa: To indicate to the bot that you are going to request an image from the NASA library.



