import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from apscheduler.schedulers.asyncio import AsyncIOScheduler

TOKEN = "8689457761:AAF3yVUbP29Am8ag-LEw9SCnwSQr6V7LkJ4"

# Твой Telegram ID (или ID группы/канала), куда бот будет слать сообщения
USER_ID = 5216014080

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Список из 10 сообщений
MESSAGES = [
    "лю тя ❤️",
    "все еще оч лю тя 💕",
    "безумна тя лю 💋",
    "ема ты красива седня 💕",
    "я б на тебя малился ❤️",
    "ты седня багиня💋",
    "ну я тебе все еще лю❤️",
    "оч лю тя❤️",
    "ема ты седня гарна💕",
    "ю тя очень сильно💋",
]


# Функция, которая будет вызываться каждый день по расписанию
async def send_daily_message():
    message_to_send = random.choice(MESSAGES)
    try:
        await bot.send_message(chat_id=USER_ID, text=message_to_send)
        print(f"Отправлено сообщение: {message_to_send}")
    except Exception as e:
        print(f"Ошибка при отправке: {e}")


@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        f""
        "прив",
        parse_mode="Markdown",
    )


async def main():
    # Настраиваем планировщик задач
    scheduler = AsyncIOScheduler(timezone="Europe/Kyiv")

    # Указываем время запуска (например, каждый день в 09:00 утра)
    scheduler.add_job(send_daily_message, "cron", hour=12, minute=0)
    scheduler.start()

    print("Бот и планировщик запущены!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())