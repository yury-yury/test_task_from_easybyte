import logging
from random import choice

from aiogram import Bot
from aiogram.filters import CommandObject
from aiogram.types import Message

from change_currency.utils import get_rate


async def get_start(message: Message, bot: Bot):
    logging.info(f'Message {message.text} is handel')
    phrases = ["Привет! Отлично выглядишь :)",
        "Хэллоу, сегодня будет отличный день!",
        "Здравствуй)) улыбнись :)"]
    await message.answer(
        f"{choice(phrases)} {message.from_user.first_name}!\n"
        f"<b>Рад тебя видеть!</b>\n"
        f"\nЯ могу отвечать на базовые команды\n"
        f"и выполнять функцию конвертации валют." )


async def get_help(message: Message, bot: Bot):
    logging.info(f'Message {message.text} is handel')
    await message.answer(
        "<b>Основные команды</b>\n"
        "/start - Начало работы с ботом\n"
        "/help - получение страницы описания команд для бота\n"
        "/convert {Количество} {Код исходной валюты} to {Код целевой валюты}\n"
        "    - конвертация заданной суммы из одной валюты в другую. Например, /convert 100 USD to EUR")


async def get_change_currency(message: Message, command: CommandObject):
    logging.info(f'Message {message.text} is handel')
    if command.args is None:
        logging.error('Arguments were not passed')
        await message.answer("Ошибка: не переданы аргументы")
        return

    try:
        count, cur_from, _, cur_to = command.args.split(' ')
        if not count.isdigit():
            logging.error('The transferred amount of the convertible currency is not a valid value.')
            raise ValueError
        if _ != 'to':
            logging.error('The to word is missing from the request arguments.')
            raise ValueError
        if len(cur_to) != 3 or not cur_to.isalpha() or not cur_to.isupper():
            logging.error('The letter code of the target currency is not valid.')
            raise ValueError
        if len(cur_from) != 3 or not cur_from.isalpha() or not cur_from.isupper():
            logging.error('The letter code of the source currency is not valid.')
            raise ValueError

    except ValueError:
        logging.error('The command format is incorrect.')
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
                                 f"Вы получите {round(int(count) / float(rate_from) * float(rate_to), 2)} {cur_to}")


async def get_goodbye(message: Message, bot: Bot):
    logging.info(f'Message {message.text} is handel')
    phrases = ["Пока! Приятного дня :)",
               "Удачи, возвращайся!",
               "До свидания, рад был пообщаться"]
    await message.answer(f"{choice(phrases)}")
