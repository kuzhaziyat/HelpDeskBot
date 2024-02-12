import telebot
from telebot import types
import config
import requests
bot = telebot.TeleBot(config.Token)

def start(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    button_phone = types.KeyboardButton(text="Отправить свой контакт", request_contact=True)
    keyboard.add(button_phone)
    return bot.send_message(message.chat.id,
                    "Вы не зарегистрированны,\n"
                    "отправтье нам свой контакт",
                    reply_markup=keyboard)

def post_contact_to_site(message):
    new_data = {
        "user_id" : message.contact.user_id,
        "phone_number" : message.contact.phone_number,
    }
    url_post = config.url_site + '/auth/'
    post_response = requests.post(url_post,data=new_data)
    print(str(post_response))
    return bot.send_message(message.chat.id,
                    "Вы не зарегистрированны,\n"
                    "отправтье нам свой контакт")