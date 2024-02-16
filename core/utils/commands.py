from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Начало работы"),
        BotCommand(command="help", description="Помощь"),
        BotCommand(command="convert", description="Конвертация валюты"),
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())