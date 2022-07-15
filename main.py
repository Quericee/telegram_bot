import time

from telegram import Update, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler
from telegram.ext import CallbackContext
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup
import requests
import urllib.parse
from bs4 import BeautifulSoup
from fake_headers import Headers
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from parser_labirint import *


def main_handler(update: Update, context: CallbackContext):
    text = update.message.text.replace(' ', '%20')
    main_url = f"https://www.labirint.ru/search/{text}/?stype=0"
    rq = requests.get(main_url)
    parse_products = parse_request(rq)
    update.message.reply_text(parse_result(parse_products))


def main():
    updater = Updater(
        token='5401890954:AAHlln3oV_nJ_9jYnrLihl7ApNLssntAbAQ',
        use_context=True
    )
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(filters=Filters.text, callback=main_handler))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
