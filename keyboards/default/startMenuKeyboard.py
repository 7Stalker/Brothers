from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

menuStart = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🧍🏻 Tana turlari')
        ],
        [
            KeyboardButton(text="📞 Biz bilan bog'lanish"),
            KeyboardButton(text='⚙️ Sozlamalar')
        ],
        [
            KeyboardButton(text='📍 Bizning manzil')
        ],
    ],
    resize_keyboard=True
)

