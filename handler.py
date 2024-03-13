import telebot
from telebot import types
import config
import requests

bot = telebot.TeleBot(config.Token)


def start(message):
    keyboard = types.ReplyKeyboardMarkup(
        row_width=1, resize_keyboard=True, one_time_keyboard=True
    )
    webApp = types.WebAppInfo("https://" + str(config.url_site))
    webAppTasks = types.WebAppInfo("https://127.0.0.1:8000")
    print(webApp)
    app = types.InlineKeyboardButton(text="Зайти в HelpDesk", web_app=webApp)
    task = types.InlineKeyboardButton(text="Зайти в список задач", web_app=webAppTasks)
    getTask = types.InlineKeyboardButton(
        text="Получить список задач",
    )

    keyboard.add(app, task, getTask)

    return bot.send_message(
        message.chat.id,
        "Здраствуйте ваш id для регистрации в HelpDesk "
        + str(message.from_user.id)
        + "\nПередайте вашему куратору ваш id",
        reply_markup=keyboard,
    )


def get_tasks_user(message):
    url_post = config.url_site + "/task/list/" + str(message.from_user.id)
    post_response = requests.get(url_post)
    return bot.send_message(message.chat.id, str(post_response.text))
