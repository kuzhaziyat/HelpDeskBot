import telebot
from telebot import types
import config
import requests

bot = telebot.TeleBot(config.Token)


def start(message):
    keyboard = types.ReplyKeyboardMarkup(
        row_width=1, resize_keyboard=True, one_time_keyboard=True
    )
    webApp = types.WebAppInfo("https://127.0.0.1:8000")
    webAppTasks = types.WebAppInfo("https://127.0.0.1:8000")

    app = types.InlineKeyboardButton(text="Зайти в HelpDesk", web_app=webApp)
    task = types.InlineKeyboardButton(text="Зайти в список задач", web_app=webAppTasks)
    vkBut = types.InlineKeyboardButton(text="Зайти", url=config.url_site)

    keyboard.add(app, task, vkBut)

    return bot.send_message(
        message.chat.id,
        "Здраствуйте ваш id для регистрации в HelpDesk "
        + str(message.from_user.id)
        + "\nПередайте вашему куратору ваш id",
        reply_markup=keyboard,
    )
