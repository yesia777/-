import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

BOT_TOKEN = "8383844434:AAFRgF3RvGV8awGib44WhNrt3YD_D7bVQEE"
CAMERA_URL = "https://твоя-ссылка.github.io/asl-camera"

dp = Dispatcher()

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🎥 Открыть камеру")],
        [KeyboardButton(text="ℹ️ Помощь")],
    ],
    resize_keyboard=True,
)

@dp.message(F.text == "/start")
async def cmd_start(message: Message):
    await message.answer(
        "<b>Привет!</b> 👋\n\n"
        "Я бот для распознавания жестов английского алфавита (ASL).\n"
        "Нажми кнопку <b>«🎥 Открыть камеру»</b>, чтобы перейти на страницу, "
        "где камера телефона будет считывать жесты в реальном времени.",
        reply_markup=keyboard,
    )

@dp.message(F.text == "🎥 Открыть камеру")
async def open_camera(message: Message):
    await message.answer(
        "Сейчас отправлю ссылку на страницу с камерой.\n\n"
        "Важно: страница должна открываться по <b>https://</b>, "
        "тогда iPhone разрешит доступ к камере.",
        reply_markup=keyboard,
    )
    await message.answer(f"Открой эту ссылку: {CAMERA_URL}")

@dp.message(F.text == "ℹ️ Помощь")
async def cmd_help(message: Message):
    await message.answer(
        "1️⃣ Нажми «🎥 Открыть камеру».\n"
        "2️⃣ Перейди по ссылке (она откроется внутри Telegram на iPhone).\n"
        "3️⃣ Разреши доступ к камере.\n"
        "4️⃣ Показывай буквы английского алфавита жестами (ASL).\n"
        "5️⃣ Страница будет в реальном времени показывать распознанные буквы "
        "и собирать слово.",
        reply_markup=keyboard,
    )

@dp.message()
async def fallback(message: Message):
    await message.answer(
        "Пока я понимаю только кнопки 😊\n"
        "Нажми «🎥 Открыть камеру» или «ℹ️ Помощь».",
        reply_markup=keyboard,
    )

async def main():
    bot = Bot(
        BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
