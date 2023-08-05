from telebot import types


def ok_button():
    inline_markup = types.InlineKeyboardMarkup()
    inline_markup.add(types.InlineKeyboardButton('OK', callback_data='OK'))

    return inline_markup