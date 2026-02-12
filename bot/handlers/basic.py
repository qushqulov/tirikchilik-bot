from telegram import (
    Update, 
    ReplyKeyboardMarkup, KeyboardButton, 
    WebAppInfo,
    InlineKeyboardMarkup, InlineKeyboardButton,
)

from telegram.ext import CallbackContext, CommandHandler, MessageHandler, Filters, CallbackQueryHandler

from ..config import contants


def start_command(update: Update, context: CallbackContext):
    update.message.reply_html(
        text=contants.welcome_msg.format(name=update.effective_user.full_name),
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(
                        text="🔥 Mahsulotlar", web_app=WebAppInfo(url="https://uzum.uz")
                    ),
                    KeyboardButton(text="📥 Savatcha"),
                ],
                [KeyboardButton(text="Hamkorlik"), KeyboardButton(text="Ma'lumotlar")],
                [
                    KeyboardButton(text="Tilni tanlash"),
                ],
            ],
            resize_keyboard=True,
        ),
    )


def cart_hendler(update: Update, context: CallbackContext):
    update.message.reply_html(
        text='<b>Sizning savatingiz bo\'sh</b>'
    )


def hamkorlik_handler(update: Update, context: CallbackContext):
    update.message.reply_html(
        text="<b>Hamkorlik uchun biz bilan bog'laning:</b>\n\n👨‍💻 Admin: @qushqulov0221"
    )


def select_lang_hendler(update: Update, context: CallbackContext):
    update.message.reply_html(
        text='<b>Tilni tanlash</b>',
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='Uzbek', callback_data='lang:uzbek'),
                    InlineKeyboardButton(text='English', callback_data='lang:english')
                ]
            ]
        )
    )


def change_lang_query(update: Update, context: CallbackContext):
    query = update.callback_query
    _, lang = query.data.split(':')
    query.answer()
    query.message.reply_text(f'Siz {lang} tilini tanladingiz.')


"""
# Buni dispatcher bor joyga qo'shishingiz shart:

updater = Updater("TOKEN_SHU_YERGA", use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start_command))
dispatcher.add_handler(MessageHandler(Filters.text("Hamkorlik"), hamkorlik_handler))
dispatcher.add_handler(MessageHandler(Filters.text("📥 Savatcha"), cart_hendler))
dispatcher.add_handler(MessageHandler(Filters.text("Tilni tanlash"), select_lang_hendler))
dispatcher.add_handler(CallbackQueryHandler(change_lang_query, pattern='^lang:'))
"""