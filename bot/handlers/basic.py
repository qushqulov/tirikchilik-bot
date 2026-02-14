from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from telegram.ext import CallbackContext

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
                [
                    KeyboardButton(text="Contact Yuborish", request_contact=True),
                    KeyboardButton(text="Lokatsiya Yuborish", request_location=True),
                ],
            ],
            resize_keyboard=True,
             one_time_keyboard=True,
        ),
    )


def cart_hendler(update: Update, context: CallbackContext):
    update.message.reply_html(
        text='<b>Sizning savatingiz bo\'sh</b>'
    ) 


def hamkorlik_hendler(update: Update, context: CallbackContext):
    update.message.reply_html(
        text=contants.hamkorlik_taxt
    )