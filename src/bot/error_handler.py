import logging

from telegram.ext import ContextTypes
from telegram import Update



async def error_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Логи ошибок при обработке обновлений."""
    logging.error(
        msg='Exception while handling an update:', exc_info=context.error
    )
