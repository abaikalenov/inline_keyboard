import logging

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.callback_datas import buy_callback
from keyboards.inline.choice_buttons import choice, pear_keyboard, apples_keyboard
from loader import dp, bot

@dp.message_handler(Command("start"))
async def show_items(message: Message):
    await message.answer(text="Choose one of item:",
                         reply_markup=choice)

@dp.callback_query_handler(text_contains="pear")
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer("you chose visit site. Good_luck.",
                              reply_markup=pear_keyboard)

@dp.callback_query_handler(buy_callback.filter(item_name="taranchello"))
async def buying_apples(call: CallbackQuery, callback_data:dict):
    await call.answer(cache_time=60)

    logging.info(f"{callback_data=}")
    quantity = callback_data.get("quantity")
    await call.message.answer(f"You chose taranchello. Good luck.",
                              reply_markup=apples_keyboard)

@dp.callback_query_handler(buy_callback.filter(item_name="alphaestate"))
async def buying_apples(call: CallbackQuery, callback_data:dict):
    await call.answer(cache_time=60)

    logging.info(f"{callback_data=}")
    quantity = callback_data.get("quantity")
    await call.message.answer(f"You chose Alpha Estate. Good luck.",
                              reply_markup=apples_keyboard)

@dp.callback_query_handler(buy_callback.filter(item_name="wauenzl"))
async def buying_apples(call: CallbackQuery, callback_data:dict):
    await call.answer(cache_time=60)

    logging.info(f"{callback_data=}")
    quantity = callback_data.get("quantity")
    await call.message.answer(f"You chose WENZLAU VINEYARD. Good luck.",
                              reply_markup=apples_keyboard)

@dp.callback_query_handler(buy_callback.filter(item_name="daumas"))
async def buying_apples(call: CallbackQuery, callback_data:dict):
    await call.answer(cache_time=60)

    logging.info(f"{callback_data=}")
    quantity = callback_data.get("quantity")
    await call.message.answer(f"You chose MAS DE DAUMAS. Good luck.",
                              reply_markup=apples_keyboard)

@dp.callback_query_handler(text="cancel")
async def cancel_buying(call: CallbackQuery):
    await call.answer("You've Canceled!",
                      show_alert=True)
    await  call.message.edit_reply_markup(reply_markup=None)