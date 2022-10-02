from ast import parse
from ctypes import util
from msilib.schema import File
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import MessageNotModified


from data import config
import keyboards as kb
from middlewares import rate_limit

from pprint import pformat
import utils
import os


def is_admin(func):
    # decorator for checking is user admin
    async def wrapped(message: types.Message, state: FSMContext):
        if message.from_user.id in config.ADMINS:
            await func(message, state)
        else:
            await message.answer("У вас нет доступа к функционалу бота, обратитесь к @pheezz")
    return wrapped


@rate_limit(limit=3)
@is_admin
# function for getting info about message in pretty format
async def cmd_info(message: types.Message, state: FSMContext) -> types.Message | str:
    await message.answer(f'<pre>{pformat(message.to_python())}</pre>',
                         parse_mode='HTML')


@rate_limit(limit=0)
@is_admin
# function for getting images from message and sending ocr result
async def cmd_ocr(message: types.Message, state: FSMContext) -> types.Message | str:
    await message.answer("Ожидайте, идет распознавание текста...")
    await message.photo[-1].download(destination_file='data/temp_ocr.png')
    await message.answer(utils.ocr())


@rate_limit(limit=0)
@is_admin
# function for getting file from message and sending converted file
async def cmd_convert(message: types.Message, state: FSMContext):
    await message.document.download(destination_file=f'data/{message.document.file_name}')
    await utils.fsm.choose_convert_ext.extention.set()
    await message.answer("Выберите формат, в который хотите конвертировать файл",
                         reply_markup=await kb.inline.convert_kb(message.document.file_name.split('.')[-1]))
    async with state.proxy() as data:
        data['file_name'] = message.document.file_name


async def cmd_convert_ext(call: types.CallbackQuery, state: FSMContext):
    await call.answer("Ожидайте, идет конвертация файла...")
    async with state.proxy() as data:
        file_name = data['file_name']
    file_format = call.data
    with open(utils.convert_file(file_name, file_format), 'rb') as file:
        await call.message.answer_document(file)

    await call.message.delete()  # delete message with keyboard
    tmp_files = [f for f in os.listdir(
        'data') if f.startswith(file_name.split('.')[0])]
    for file in tmp_files:
        os.remove(f'data/{file}')
    await state.finish()
