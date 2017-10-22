# my first Telegram Bot on Python3.5
"""
I learn Python3.5
"""

# to import a library pyTelegramBotAPI
import telebot

# to import a file with our constants
from org.companyname.infobot import constants

# put Token API of your Telegram Bot to file "constants.py" to variable "token"
bot = telebot.TeleBot(constants.token)

# send a message to chat with the number id
# look your chat id with the method getUpdates from https://api.telegram.org/
# id = 1234567890

# bot.send_message(id, "test from MyBot")

# to receive the updates from server
updates = bot.get_updates()

# for print the messages of updates to console
print(updates)