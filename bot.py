import os
import telebot

TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я — Боречка, твой кактус-бот.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Ты написал: " + message.text)

bot.polling(none_stop=True)