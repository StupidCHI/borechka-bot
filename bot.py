from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
import os

# Токен из переменной окружения
BOT_TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    web_app_btn = KeyboardButton(
        text="Запустить Боречку",
        web_app=WebAppInfo(url="https://borechka-bot.vercel.app")  # <-- сюда вставлен твой домен
    )
    markup.add(web_app_btn)

    await message.answer(
        "Привет! Я — Боречка, твой кактус-бот. Нажми кнопку ниже, чтобы начать!",
        reply_markup=markup
    )

if __name__ == "__main__":
    executor.start_polling(dp)