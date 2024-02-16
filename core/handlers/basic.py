from aiogram import Bot
from aiogram.filters import CommandObject
from aiogram.types import Message

from change_currency.utils import get_rate


async def get_start(message: Message, bot: Bot):
    await message.answer(
        f"Привет {message.from_user.first_name}!\n"
        f"<b>Рад тебя видеть!</b>\n"
        f"\nЯ могу отвечать на базовые команды\n"
        f"и выполнять функцию конвертации валют." )


async def get_help(message: Message, bot: Bot):
    await message.answer(
        f"Основные команды\n/start - Начало работы с ботом\n/help - получение страницы описания команд для бота" )


async def get_change_currency(message: Message, command: CommandObject):
    if command.args is None:
        await message.answer("Ошибка: не переданы аргументы")
        return

    try:
        count, cur_from, _, cur_to = command.args.split(' ')
        if not count.isdigit():
            raise ValueError
        if len(cur_to) != 3 or not cur_to.isalpha() or not cur_to.isupper():
            raise ValueError
        if len(cur_from) != 3 or not cur_from.isalpha() or not cur_from.isupper():
            raise ValueError

    except ValueError:
        await message.answer("Ошибка: неправильный формат команды. Пример:\n"
                             "/convert 100 USD to EUR")
        return

    else:
        rate_from = get_rate(cur_from)
        rate_to = get_rate(cur_to)
        if None in [rate_to, rate_from]:
            await message.answer("Указанные названия валют не найдены в базе данных")
        else:
            await message.answer(f"При обмене {count} {cur_from}\n "
                                 f"Вы получите {round(int(count) / float(rate_from) * float(rate_to), 2)}")

