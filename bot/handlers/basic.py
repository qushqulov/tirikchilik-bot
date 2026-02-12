from telegram import (
    Update, 
    ReplyKeyboardMarkup, KeyboardButton, 
    WebAppInfo,
    InlineKeyboardMarkup, InlineKeyboardButton,
)

from telegram.ext import CallbackContext, MessageHandler, Filters

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
    _, lang = update.callback_query.data.split(':')
    update.callback_query.message.reply_text(f'siz {lang} ni tanladingiz.')

