from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

catKeyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='➡️  EKTOMORF  ✅'),

        ],
        [

            KeyboardButton(text='➡️  MEZOMORF  ✅'),

        ],
        [

            KeyboardButton(text='➡️  ENDOMORF  ✅'),
        ],
       [
            KeyboardButton(text='⬅️ORTGA'),
            KeyboardButton(text='BOSHIGA🔄'),
        ],

    ],
    resize_keyboard=True
)