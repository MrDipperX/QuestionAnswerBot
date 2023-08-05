from loader import bot
from config.config import CHAT_ID
from keyboards.keyboards import ok_button


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

            bot.send_message(CHAT_ID, f'User: `{message.from_user.id}` , @{message.from_user.username}, '
                                      f'\nQuestion: {get_message_bot}', parse_mode='MARKDOWN', reply_markup=ok_button())
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
