import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from config.config import TELEGRAM_TOKEN_BOT
from handlers import adopt, browse, feedback, meet, start, support, base_handler

# Налаштування логування
logging.basicConfig(level=logging.INFO)

# Ініціалізація бота
bot = Bot(token=TELEGRAM_TOKEN_BOT)

# Ініціалізація диспетчера (нова архітектура aiogram 3)
dp = Dispatcher()

# Підключення роутерів
dp.include_router(start.router)
dp.include_router(browse.router)
dp.include_router(adopt.router)
dp.include_router(meet.router)
dp.include_router(feedback.router)
dp.include_router(support.router)
dp.include_router(base_handler.router)  # Підключаємо роутер з base_handler


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
