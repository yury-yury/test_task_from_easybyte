from aiogram.filters import BaseFilter
from aiogram.types import Message


class GreetingFilter(BaseFilter):
    def __init__(self) -> None:
        self.word_list = ['hello', 'hi', 'hey', 'привет', 'здравствуй', 'здравствуйте', 'приветствую', 'добрый']

    async def __call__(self, message: Message) -> bool:
        for word in message.text.lower().split(' '):
            if word in self.word_list:
                return True
        return False
