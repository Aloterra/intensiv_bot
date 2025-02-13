import asyncio

import schedule
from telebot.async_telebot import AsyncTeleBot

import days
from config import *
from handlers import register_handlers

bot = AsyncTeleBot(TOKEN)


async def schedule_checker():
    while True:
        schedule.run_pending()
        await asyncio.sleep(1)


def run_day_checker():
    asyncio.create_task(days.day_checker())


async def main():
    await register_handlers(bot)

    schedule.every(5).seconds.do(run_day_checker)
    asyncio.create_task(schedule_checker())
    await bot.infinity_polling()
    configure_logging()


if __name__ == '__main__':
    asyncio.run(main())
