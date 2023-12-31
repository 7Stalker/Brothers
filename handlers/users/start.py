import logging

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.startMenuKeyboard import menuStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    logging.info(message)
    await message.answer(f"Assalomu aleykum, {message.from_user.full_name}! BROTHER SPORT ZALIGA xush kelibsiz!!!", reply_markup=menuStart)