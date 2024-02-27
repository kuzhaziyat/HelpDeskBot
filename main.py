from telebot import types
import telebot
import handler
import config


bot = telebot.TeleBot(config.Token)


@bot.message_handler(
    content_types=[
        "text",
        "photo",
        "video",
        "document",
    ]
)
def get_text_message(message):
    if message.text == "/start":
        handler.start(message)


if __name__ == "__main__":
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
    bot.polling(none_stop=True, interval=1)
