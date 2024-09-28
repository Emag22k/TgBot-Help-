import telebot

bot=telebot.TeleBot("7921809355:AAH5QgnbNT9pWh2TvZby8zFd13ybkthQSu4")

@bot.message_handler(commands=["start"])
def start(message):
    user_id=message.from_user.id
    bot.send_message(user_id, "Приветстую тебя! Введи свое имя:")

    bot.register_next_step_handler(message, get_name)


def get_name(message):
    user_id=message.from_user.id
    user_name=message.text
    bot.send_message(user_id, f"Приятно познакомиться {user_name}!")


@bot.message_handler(commands=["help"])
def help(message):
    user_id=message.from_user.id
    bot.send_message(user_id, "Как я могу вам помочь?")



bot.polling(non_stop=True)
