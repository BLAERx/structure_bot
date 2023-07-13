import asyncio
import os

from dotenv import load_dotenv
from bot.handlers.user_handlers import register_user_handlers

from aiogram import Bot, Dispatcher, types
from bot.tk import TOKEN_API

def register_handler(dp: Dispatcher) -> None:
    register_user_handlers(dp)


async def main() -> None:
    """Entry point"""
    token = TOKEN_API
    bot = Bot(token)
    dp = Dispatcher(bot)

    register_handler(dp)
    try:
        await dp.start_polling()
    except Exception as _ex:
        print(f'There is exception -- {_ex}')

if __name__ == "__main__":
    asyncio.run(main())