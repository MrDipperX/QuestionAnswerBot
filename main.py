from config import TOKEN, CHAT_ID
from telebot import TeleBot
from telebot import types


bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, f'Hello, dear {message.from_user.first_name}. '
                                           f'Write me the question in which you are interested.')


@bot.message_handler(content_types=['text'])
def mess(message):
    try:
        get_message_bot = message.text.strip()

        if get_message_bot[:6].isdigit() and str(message.chat.id) == CHAT_ID:
            splited_text = get_message_bot.split('|')
            user_id = splited_text[0]
            answer = splited_text[1]
            bot.send_message(user_id, answer)

        elif str(message.chat.id) != CHAT_ID:
            inline_markup = types.InlineKeyboardMarkup()
            inline_markup.add(types.InlineKeyboardButton('OK', callback_data='OK'))
            bot.send_message(CHAT_ID, f'User: `{message.from_user.id}` , @{message.from_user.username}, '
                                      f'\nQuestion: {get_message_bot}', parse_mode='MARKDOWN', reply_markup=inline_markup)
    except Exception as e:
        print(e)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    try:
        if call.data == "OK":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=call.message.text+"\n🟢",)
    except Exception as e:
        print(e)


def main_loop():
    bot.polling(none_stop=True)


if __name__ == '__main__':
    main_loop()
