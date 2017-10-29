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

"""for print last message of the update
# last_updates = updates[-1]
# message_from_user = last_updates.message

# print(message_from_user)
"""

# print to console info about bot
print(bot.get_me())

# a function "log" for logging a bot job
def log(message, answer):
    print("-----------")
    from datetime import datetime
    print(datetime.now())
    print("Message from {0}, {1}, id = {2}\nMessage text: {3}"
          .format(message.from_user.first_name, message.from_user.last_name,
                  str(message.from_user.id), message.text))
    print("Bot answer: " + answer)



@bot.message_handler(commands=["start"])
def handle_start(message):
    print("I received a command /start")

    # create userkeyboard, resize = true, autohide=true
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row("/start", "/stop", "/help", "/settings")
    user_markup.row("/foto", "/audio", "/documents")
    user_markup.row("/sticker", "/video", "/voice", "/location")

    # send a message to a user with new keyboard
    bot.send_message(message.from_user.id, constants.command_start, reply_markup=user_markup)

@bot.message_handler(commands=["settings"])
def handle_settings(message):
    print("I received a command /settings")
    bot.send_message(message.from_user.id, constants.command_settings)

@bot.message_handler(commands=["help"])
def handle_help(message):
    print("I received a command /help")
    bot.send_message(message.from_user.id, constants.command_help)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    # print("I received a text")

    if message.text == "Hi":
        bot.send_message(message.from_user.id, constants.answer_hi)
        log(message, constants.answer_hi)
    elif message.text == "Bye":
        bot.send_message(message.from_user.id, constants.answer_bye)
        log(message, constants.answer_bye)
    else:
        bot.send_message(message.from_user.id, constants.answer_default)
        log(message, constants.answer_default)

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