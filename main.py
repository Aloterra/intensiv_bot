import asyncio

from telebot.async_telebot import AsyncTeleBot

from config import *
from handlers import register_handlers

bot = AsyncTeleBot(TOKEN)


async def main():
    await register_handlers(bot)
    await bot.infinity_polling()


if __name__ == '__main__':
    asyncio.run(main())
