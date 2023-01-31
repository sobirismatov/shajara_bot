import os
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (
    Updater,
    CallbackContext,
    CommandHandler,
    CallbackQueryHandler
)

TOKEN = os.environ['TOKEN']
def start(update:Update,context:CallbackContext):
    inline_keyboard = [ 
        [
            InlineKeyboardButton(text='Ajdod_1', callback_data='Ajdod_1'),
            InlineKeyboardButton(text="Ma'lumot_1", callback_data="Ma'lumot_1") ,
            InlineKeyboardButton(text='Avlod_1', callback_data='Avlod_1')
        ],
        [
        #     InlineKeyboardButton(text='x', callback_data='close')
         ]
    ]
    update.message.reply_html(
            text="<b>Assalomu alaylum!</b>\n\n<i>Ismatovlar shajara botga xush kelibsiz!!</i>", 
            reply_markup=InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
        )
def Ajdod_1(update:Update,context:CallbackContext):
    pass
def main():
    updater = Updater(token=TOKEN)
    dp = updater.dispatcher

    dp.add_handler(handler=CommandHandler(command='start', callback=start))

    # dp.add_handler(handler=MessageHandler(filters=filters.Filters.text('Ajdod_1'), callback=Ajdod_1))
    # dp.add_handler(handler=MessageHandler(filters=filters.Filters.text('👎'), callback=dislike))

    # dp.add_handler(handler=MessageHandler(filters=filters.Filters.all, callback=default))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
