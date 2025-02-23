import telebot
import datetime
from telebot import types

from bot_token import bot_token
# import shedule
# import classes
# from save_users import save_users

from init import initialize

# Путь к директории с расписанием
DIR_SCHEDULE = r'./schedule'

# Расписание всех классов
schedule = {}
classes = []
save_users = {}

bot = telebot.TeleBot(bot_token)


def get_start_keyboard():
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton(text="Мое расписание"))
    return markup


def grade_keyboard():
    markup = types.ReplyKeyboardMarkup()
    for i in classes:
        markup.add(types.KeyboardButton(text=i))
    return markup


@bot.message_handler(commands=["start"])
def start_command(message):
    bot.send_message(chat_id=message.chat.id,
                     text="hello",
                     reply_markup=get_start_keyboard())


@bot.message_handler(content_types=['text'])
def hello_world(message: telebot.types.Message):
    if message.text == "Мое расписание":
        if message.from_user.id in save_users:
            print(message.from_user)
            print(message.from_user.id)
            print(save_users)
            print(save_users[message.from_user.id])
            print(schedule)
            print(datetime.datetime.now().weekday())
            bot.send_message(chat_id=message.chat.id,
                             text=save_users[message.from_user.id] + '\n'
                            + schedule[save_users[message.from_user.id]][datetime.datetime.now().weekday()],
                             reply_markup=get_start_keyboard())
            bot.delete_message(chat_id=message.chat.id,
                               message_id=message.message_id)
        else:
            bot.send_message(chat_id=message.chat.id,
                             text="я тебя не помню, напиши в каком ты классе\nвыбери свой класс",
                             reply_markup=grade_keyboard())
            bot.register_next_step_handler(message, adding_new_user)
    else:
        bot.reply_to(message, "я тебя не понимаю")


def adding_new_user(message: telebot.types.Message):
    if message.text in classes:
        save_users[message.from_user.id] = message.text
        bot.send_message(chat_id=message.chat.id,
                         text="ура мы тебя запомнили",
                         reply_markup=types.ReplyKeyboardRemove())
    else  :
        bot.send_message(chat_id=message.chat.id,
                         text="попробуй еще раз, нажми на кнопку")
        bot.register_next_step_handler(message, adding_new_user)




def run():

    initialize(DIR_SCHEDULE, schedule, classes)
    bot.infinity_polling()


if __name__ == '__main__':
    run()