import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command

from core.filters.goodbay import GoodbyeFilter
from core.filters.greetings import GreetingFilter
from core.handlers.basic import get_start, get_help, get_change_currency, get_goodbye
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
        filename="bot_log.log",
        filemode="a",
        format="%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s.%(funcName)s(%(lineno)d) - %(message)s",
    )

    bot = Bot(token=settings.TG_TOKEN, parse_mode="HTML")

    dp = Dispatcher()

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.message.register(get_start, Command(commands=["start", "run"]))
    dp.message.register(get_help, Command(commands='help'))
    dp.message.register(get_change_currency, Command(commands='convert'))
    dp.message.register(get_start, GreetingFilter())
    dp.message.register(get_goodbye, GoodbyeFilter())

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())