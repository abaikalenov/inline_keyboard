from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import URL_JIHC, URL_WINE
from keyboards.inline.callback_datas import buy_callback

choice = InlineKeyboardMarkup(row_width=2)

buy_pear = InlineKeyboardButton(text="SITE", callback_data=buy_callback.new(item_name="pear", quantity=1))
choice.insert(buy_pear)

buy_apples = InlineKeyboardButton(text="Taranchello", callback_data="buy:taranchello:1")
choice.insert(buy_apples)

author = InlineKeyboardButton(text="alpha estate", callback_data="buy:alphaestate:5")
choice.insert(author)

wenzlau = InlineKeyboardButton(text="WENZLAU VINEYARD", callback_data="buy:wauenzl:5")
choice.insert(wenzlau)

MAS = InlineKeyboardButton(text="MAS DE DAUMAS", callback_data="buy:daumas:5")
choice.insert(MAS)

cancel_button = InlineKeyboardButton(text="Cancel", callback_data="cancel")
choice.insert(cancel_button)

pear_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Our shop", url=URL_WINE)
    ]
])
apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="tracking", url=URL_JIHC)
    ]
])