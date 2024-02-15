import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import Command

from core.handlers.basic import get_start
from core.settings import settings
from core.utils.commands import set_commands


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.ADMIN_ID, "Бот запущен.")


async def stop_bot(bot: Bot):
    await bot.send_message(settings.ADMIN_ID, "Бот остановлен.")


async def start():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s.%(funcName)s(%(lineno)d) - %(message)s",
    )

    bot = Bot(token=settings.TG_TOKEN, parse_mode="HTML")

    dp = Dispatcher()

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.message.register(get_start, Command(commands=["start", "run"]))

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())