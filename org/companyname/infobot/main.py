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

@bot.message_handler(commands=["start"])
def handle_text(message):
    print("I received a command /start")
    bot.send_message(message.from_user.id, "Start info of your Bot")

@bot.message_handler(commands=["settings"])
def handle_text(message):
    print("I received a command /settings")
    bot.send_message(message.from_user.id, "Settings of your Bot")

@bot.message_handler(commands=["help"])
def handle_text(message):
    print("I received a command /help")
    bot.send_message(message.from_user.id, "Help info about your Bot")

@bot.message_handler(content_types=["text"])
def handle_text(message):
    print("I received a text")
    if message.text == "Hi":
        bot.send_message(message.from_user.id, "Hi user!")
    elif message.text == "Bye":
        bot.send_message(message.from_user.id, "Bye-bye!")
    else:
        bot.send_message(message.from_user.id, "I am a InfoBot")

@bot.message_handler(content_types=["document"])
def handle_document(message):
    print("I received a document")

@bot.message_handler(content_types=["audio"])
def handle_audio(message):
    print("I received a audio")

@bot.message_handler(content_types=["photo"])
def handle_photo(message):
    print("I received a photo")

@bot.message_handler(content_types=["sticker"])
def handle_sticker(message):
    print("I received a sticker")

bot.polling(none_stop=True, interval=1)