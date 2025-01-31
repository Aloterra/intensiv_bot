from .buttons import register_buttons_handlers
from .start import register_start_handlers


async def register_handlers(bot):
    await register_buttons_handlers(bot)
    await register_start_handlers(bot)
