from aiogram.filters import BaseFilter
from aiogram.types import Message


class GoodbyeFilter(BaseFilter):
    def __init__(self) -> None:
        self.word_list = ['goodbye', 'bye', 'пока', 'прощай', 'до']

    async def __call__(self, message: Message) -> bool:
        for word in message.text.lower().split(' '):
            if word in self.word_list:
                return True
        return False
