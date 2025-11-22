# bot.py
import telebot
from funk import meme_parsing, it_meme_parsing

key = "ВАШ ТОКЕН"
bot = telebot.TeleBot(key)

@bot.message_handler(commands=["start"])
def hello(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton("Обычный мем")
    btn2 = telebot.types.KeyboardButton("IT мем")
    markup.add(btn1, btn2)

    bot.send_message(
        message.chat.id,
        "Привет! Я мем-бот.\nВыбери, какие мемы хочешь:",
        reply_markup=markup
    )

@bot.message_handler(func=lambda m: True)
def buttons(message):
    if message.text == "Обычный мем":
        img = meme_parsing()
        if img:
            bot.send_photo(message.chat.id, img)
        else:
            bot.send_message(message.chat.id, "😔 Не удалось найти мемы, попробуй позже.")
        return

    if message.text == "IT мем":
        img = it_meme_parsing()
        if img:
            bot.send_photo(message.chat.id, img)
        else:
            bot.send_message(message.chat.id, "😔 Не удалось найти IT-мемы, попробуй позже.")
        return

    bot.send_message(message.chat.id, "Выбери кнопку 🙂")

if __name__ == "__main__":
    bot.infinity_polling()














