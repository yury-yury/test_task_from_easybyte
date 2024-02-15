from aiogram import Bot
from aiogram.types import Message


async def get_start(message: Message, bot: Bot):
    await message.answer(
        f"Привет {message.from_user.first_name}!\n<b>Рад тебя видеть!</b>\n\nЯ могу отвечать на базовые команды\nи выполнять функцию конвертации валют." )
