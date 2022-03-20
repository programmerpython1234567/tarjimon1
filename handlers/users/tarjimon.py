from aiogram import types
from loader import dp
from googletrans import Translator


tarjimon = Translator()
@dp.message_handler()
async def bot_echo(message: types.Message):
    til = tarjimon.detect(text=message.text).lang
    matn = message.text
    if til == 'uz':
        tarjima_qilish = tarjimon.translate(text=matn, dest='en', src='uz').text
        await message.answer(text=f'{tarjima_qilish}')
    elif til == 'en':
        tarjima_qilish = tarjimon.translate(text=matn, dest='uz', src='en').text
        await message.answer(text=f'{tarjima_qilish}')

    elif til == 'ru':
        tarjima_qilish = tarjimon.translate(text=matn, dest='uz', src='ru').text
        await message.answer(text=f'{tarjima_qilish}')
    elif til == 'uz':
        tarjima_qilish = tarjimon.translate(text=matn, dest='ru', src='uz').text
        await message.answer(text=f'{tarjima_qilish}')

    elif til == 'en':
        tarjima_qilish = tarjimon.translate(text=matn, dest='ru', src='en').text
        await message.answer(text=f'{tarjima_qilish}')
    elif til == 'ru':
        tarjima_qilish = tarjimon.translate(text=matn, dest='en', src='ru').text
        await message.answer(text=f'{tarjima_qilish}')
