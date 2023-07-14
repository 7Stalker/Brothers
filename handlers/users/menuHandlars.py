import logging
from aiogram import Bot

from aiogram.types import Message, CallbackQuery

from keyboards.default.startMenuKeyboard import menuStart
from keyboards.default.tanaTurlari import catKeyboard
from keyboards.inline.exerciseKeyboard import ektomorfMenu, mezomorfMenu, endomorfMenu
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from loader import dp


CONTACT_HELP = """
      <b>BIZ BILAN BOG'LANISH</b>
      
📲<b>TELEFON:</b>   +998 94 183 33 39

🎞<b>INSTAGRAM:</b>  https://instagram.com/isamurodov_doniyor?igshid=ZDdkNTZiNTM=

💬<b>TELEGRAM:</b>  @isamurodov_bot

📹<b>YOUTUBE:</b>

"""

#Bosh menu
@dp.message_handler(text="🧍🏻 Tana turlari")
async def send_link(message: Message):
    photo_url = "http://telegra.ph//file/d324414356252d4ad7515.jpg"
    await message.answer_photo(photo_url, caption=f"<b>1.EKTOMORF</b> 👉 Ushbu tur ichki organlarning yomon rivojlanishi, tana vaznining pastligi, mo'rtlik va noziklik bilan tavsiflanadi.\n\n"
                                                 f"<b>2.MEZOMORF</b> 👉 Tananing mutanosib rivojlanishi, yaxshi jismoniy rivojlanishi va aqliy barqarorligi bo'lgan odamlar turi.\n\n"
                                                 f"<b>3.ENDOMORF</b> 👉 Ichki organlarning haddan tashqari rivojlanishi va tana yog'i tufayli ortiqcha vaznli odamlar.\n\n"
                               ,parse_mode="HTML")

    await message.answer(f"Tana turlaridan birini tanlang", reply_markup=catKeyboard)
    await message.delete()

#Contact
@dp.message_handler(text="📞 Biz bilan bog'lanish")
async def send_contact(message: Message):
    await message.answer(text=CONTACT_HELP,
                         parse_mode="HTML")



# LOCATION
@dp.message_handler(text="📍 Bizning manzil")
async def send_locations(message: Message):
    await message.answer_location(latitude=39.9121453,
                                  longitude=66.2459115)


@dp.message_handler(text="BOSHIGA🔄")
async def send_link(message: Message):
    await message.answer(f"Asosiy menudasiz", reply_markup=menuStart)
    await message.delete()


@dp.message_handler(text="⬅️ORTGA")
async def send_link(message: Message):
    await message.answer(f"Oldingi menudasiz", reply_markup=menuStart)
    await message.delete()


# Tana turlari menusi
@dp.message_handler(text_contains="EKTOMORF")
async def select_menu(message: Message):
    # await message.answer(reply_markup=ReplyKeyboardRemove())
    await message.answer(
        f"1.Ushbu tur ichki organlarning yomon rivojlanishi, tana vaznining pastligi, mo'rtlik va noziklik bilan tavsiflanadi.",
        reply_markup=ektomorfMenu)
    await message.delete()



@dp.message_handler(text_contains="MEZOMORF")
async def select_menu(message: Message):
    await message.answer(f"2.Tananing mutanosib rivojlanishi, yaxshi jismoniy rivojlanishi va aqliy barqarorligi bo'lgan odamlar turi.", reply_markup=mezomorfMenu)
    await message.delete()


@dp.message_handler(text_contains="ENDOMORF")
async def send_message(message: Message):
    await message.answer(f"3.Ichki organlarning haddan tashqari rivojlanishi va tana yog'i tufayli ortiqcha vaznli odamlar.", reply_markup=endomorfMenu)

@dp.message_handler(text="⬅️ORTGA")
async def send_link(message: Message):
    await message.answer(f"Oldingi menudasiz", reply_markup=menuStart)
    await message.delete()


@dp.callback_query_handler(text="mashq")
async def all_exercise(call: CallbackQuery):
    photo_url1="http://telegra.ph//file/034f13075c84ed7d50947.jpg"
    await call.message.answer_photo(photo_url1,
                                    caption=f"1-упражнение: Жим штанги лежа на прямой скамье\n"
                                    f"Подходы: 3 x 12 шт  \nОтдыхаем между подходами:1.5 мин\n\nОтдыхаем между упражнениями:2 мин"
                                    )
    photo_url2 = "http://telegra.ph//file/c5ffb0e34ae1afab4d05b.jpg"
    await call.message.answer_photo(photo_url2,
                                    caption=f"2-упражнение: Жим гантель под углом 45 градусов\n"
                                            f"Подходы: 3 x 12 шт  \nОтдыхаем между подходами:1.5 мин\n\nОтдыхаем между упражнениями:2 мин"
                                    )
    photo_url3 = "http://telegra.ph//file/4980695769af2128945da.jpg"
    await call.message.answer_photo(photo_url3,
                                    caption=f"3-упражнение: Отжимания от пола\n"
                                            f"Подходы: 3 x 15 шт  \nОтдыхаем между подходами:1.5 мин\n\nОтдыхаем между упражнениями:2 мин"
                                    )
    photo_url4 = "http://telegra.ph//file/552f562cd198990702c34.jpg"
    await call.message.answer_photo(photo_url4,
                                    caption=f"4-упражнение: Штанга бицепс стоя\n"
                                            f"Подходы: 3 x 12 шт  \nОтдыхаем между подходами:1.5 мин\n\nОтдыхаем между упражнениями:2 мин"
                                    )
    photo_url5 = "http://telegra.ph//file/e9c029b0a0879bfd6716d.jpg"
    await call.message.answer_photo(photo_url5,
                                    caption=f"5-упражнение: Гантелей на бицепс сидя по очереди\n"
                                            f"Подходы: 3 x 12 шт  \nОтдыхаем между подходами:1.5 мин\n\n\nОтдыхаем между упражнениями:2 мин"
                                    )
    await call.answer(cache_time=60)
