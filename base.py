import logging
import sqlite3

import aiosqlite

log = logging.getLogger(__name__)


async def new_user(user_id, username, name, phone, email, order_id):
    async with aiosqlite.connect('database.db') as db:
        try:
            await db.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (user_id, f'@{username}', name, phone,
                                                                                   email, False, order_id, 0))
        except sqlite3.IntegrityError:
            await db.execute("UPDATE users SET day = 0 WHERE user_id == ?", (user_id,))
        await db.commit()
        return 1


async def user_day(user_id):
    async with aiosqlite.connect('database.db') as db:
        async with db.execute("SELECT day FROM users WHERE user_id == ?", (user_id,)) as cursor:
            current_day = await cursor.fetchone()
            return current_day[0]


async def update_day(user_id):
    async with aiosqlite.connect('database.db') as db:
        await db.execute("UPDATE users SET day = day+1 WHERE user_id == ?", (user_id,))
        await db.commit()
        return 1


async def reset_day(user_id):
    async with aiosqlite.connect('database.db') as db:
        await db.execute("UPDATE users SET day = 1 WHERE user_id == ?", (user_id,))
        await db.commit()
        return 1


async def update_block(user_id, is_block):
    async with aiosqlite.connect('database.db') as db:
        await db.execute("UPDATE users SET is_block = ? WHERE user_id == ?", (is_block, user_id))
        await db.commit()
        return 1


async def user_is_block(user_id):
    async with aiosqlite.connect('database.db') as db:
        async with db.execute("SELECT is_block FROM users WHERE user_id == ?", (user_id,)) as cursor:
            is_block = await cursor.fetchone()
            return is_block[0]


async def orders():
    async with aiosqlite.connect('database.db') as db:
        await db.execute("""CREATE TABLE IF NOT EXISTS users(
                                            user_id INTEGER UNIQUE,
                                            username CHAR,
                                            name CHAR,
                                            phone CHAR,
                                            email CHAR,
                                            is_block BOOL,
                                            order_id INTEGER,
                                            day INTEGER
                                            )""")
        async with db.execute("SELECT order_id FROM users ") as cursor:
            orders_ids = [i[0] for i in await cursor.fetchall()]
            return orders_ids


async def all_users():
    async with aiosqlite.connect('database.db') as db:
        async with db.execute("SELECT user_id FROM users") as cursor:
            users_ids = [i[0] for i in await cursor.fetchall()]
            return users_ids
