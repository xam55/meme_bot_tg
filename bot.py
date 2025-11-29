import telebot
from database import init_bd
from funk import meme_parsing, get_random_it_meme
from database import init_bd,add_user
key = "ВАШ_ТОКЕН"
bot = telebot.TeleBot(key)

@bot.message_handler(commands=["start"])
def hello(message):

    user_id = message.from_user.id
    username = message.from_user.username or f"user_{user_id}"
    add_user(user_id, username)

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
        img = get_random_it_meme()
        if img:
            bot.send_photo(message.chat.id, "ибра скуф")
        else:
            bot.send_message(message.chat.id, "ибра скуф")
        return

    bot.send_message(message.chat.id, "Выбери кнопку 🙂")


if __name__ == "__main__":
    init_bd()
    bot.infinity_polling()














