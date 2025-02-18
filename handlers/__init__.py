from .buttons import register_buttons_handlers
from .message_handlers import register_start_handlers
from .payment_handlers import register_payment_handlers


async def register_handlers(bot):
    await register_buttons_handlers(bot)
    await register_start_handlers(bot)
    await register_payment_handlers(bot)
