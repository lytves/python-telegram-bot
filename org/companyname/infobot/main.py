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
# updates = bot.get_updates()

# for print the messages of updates to console
# print(updates)

# last_updates = updates[-1]
# message_from_user = last_updates.message

# print(message_from_user)

@bot.message_handler(content_types=["commands"])
def handle_command(message):
    print("I received a command")

@bot.message_handler(content_types=["text"])
def handle_command(message):
    print("I received a text")

@bot.message_handler(content_types=["document"])
def handle_command(message):
    print("I received a document")

@bot.message_handler(content_types=["audio"])
def handle_command(message):
    print("I received a audio")

@bot.message_handler(content_types=["photo"])
def handle_command(message):
    print("I received a photo")

@bot.message_handler(content_types=["sticker"])
def handle_command(message):
    print("I received a sticker")

bot.polling(none_stop=True, interval=1)