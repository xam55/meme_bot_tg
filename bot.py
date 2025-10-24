import telebot
from funk import meme_parsing

key = "7937720296:AAEwI3Fo4X2-wOzbnJm2ohzRSt3_2VxUQ4Y"
bot = telebot.TeleBot(key)

@bot.message_handler(commands=["start"])
def hello(message):
    bot.send_message(
        message.chat.id,
        "Привет! Я мем-бот.\nВведи /meme для получения мемов."
    )

@bot.message_handler(commands=["meme"])
def meme(message):
    meme_content = meme_parsing()
    bot.send_photo(message.chat.id, meme_content)

bot.infinity_polling()












