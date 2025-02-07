import logging

import aiosqlite

log = logging.getLogger(__name__)


async def new_user(user_id, order_id):
    async with aiosqlite.connect('database.db') as db:
        await db.execute("""CREATE TABLE IF NOT EXISTS users(
                                user_id INTEGER,
                                is_block BOOL,
                                order_id INTEGER,
                                day INTEGER
                                )""")
        await db.execute("INSERT INTO users VALUES (?, ?, ?, ?)", (user_id, False, order_id, 1))
        return 1


async def user_day(user_id):
    async with aiosqlite.connect('database.db') as db:
        async with db.execute("SELECT day FROM users WHERE user_id == ?", (user_id,)) as cursor:
            current_day = await cursor.fetchone()
            return current_day


async def update_day(user_id):
    async with aiosqlite.connect('database.db') as db:
        await db.execute("UPDATE users SET day = day+1 WHERE user_id == ?", (user_id,))
        return 1


async def update_block(user_id, is_block):
    async with aiosqlite.connect('database.db') as db:
        await db.execute("UPDATE users SET is_block = ? WHERE user_id == ?", (is_block, user_id))
        return 1


async def orders():
    async with aiosqlite.connect('database.db') as db:
        async with db.execute("SELECT order_id FROM users ") as cursor:
            orders_ids = [i[0] for i in await cursor.fetchall()]
            return orders_ids
