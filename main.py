from telegram import Update
from telegram.ext import Updater
from telegram.ext import CallbackContext
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup

button_help = "Помощь"


def message_handler(update: Update, context: CallbackContext):
    text = update.message.text
    reply_markup = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text=button_help)
        ],
    ], resize_keyboard=True)
    update.message.reply_text(text='Obeme', reply_markup=reply_markup)


def main():
    updater = Updater(
        token='5401890954:AAHlln3oV_nJ_9jYnrLihl7ApNLssntAbAQ',
        use_context=True
    )
    updater.dispatcher.add_handler(MessageHandler(filters=Filters.text, callback=message_handler))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
