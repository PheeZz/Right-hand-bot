from loguru import logger


from aiogram import types
from aiogram.dispatcher import FSMContext

from middlewares import rate_limit
import keyboards as kb

from utils import parser


@rate_limit(limit=5)
async def cmd_start(message: types.Message) -> types.Message | str:
    await message.answer(f"Привет,{message.from_user.full_name}!\nВот что я умею:\n\n🔹Распознавать текст на фото\nДля этого просто отправь мне фотографию с текстом\n🔹Конвертировать файлы\n🔹Собирать информацию с поста instagram\n\
Для этого просто отправь мне сслыку на пост")


@rate_limit(limit=3)
async def instagram_description(message: types.Message) -> types.Message | str:
    await message.answer(parser.get_description(message.text))