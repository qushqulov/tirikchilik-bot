from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
)

from .config import settings
from .handlers import (
    start_command,
    cart_hendler,
)


def main() -> None:
    updater = Updater(settings.BOT_TOKEN)
    dispatcher = updater.dispatcher

    # comand handlers
    dispatcher.add_handler(CommandHandler(command="start", callback=start_command))

    # messge handlers
    dispatcher.add_handler(MessageHandler(
        filters=Filters.text('📥 Savatcha'),
        callback=cart_hendler
    ))

    updater.start_polling()
    updater.idle()
