from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loguru import logger


async def menu_kb():
    """returns inline keyboard with menu items"""
    kb = InlineKeyboardMarkup(row_width=2,)
    buttons = [
        InlineKeyboardButton(
            text='Search',
            callback_data='search'),

        InlineKeyboardButton(
            text='Sample',
            callback_data='sample'),
        InlineKeyboardButton(
            text='Home',
            callback_data='home'),
    ]
    for button in buttons:
        kb.insert(button)

    kb.add(InlineKeyboardButton(
        text='Help',
        callback_data='help'),)

    kb.add(InlineKeyboardButton(
        text='❌Close❌', callback_data='close_menu'))

    return kb


async def convert_kb(file_format: str):
    formats_doc = ['md', 'doc', 'docx', 'pdf', 'txt']
    if file_format in formats_doc:
        try:
            formats_doc.remove('doc')
            formats_doc.remove('docx')
            formats_doc.remove(file_format)
        except ValueError:
            logger.warning(
                'ValueError while removing doc/docx from formats_doc')

        kb = InlineKeyboardMarkup(row_width=2)
        buttons = [InlineKeyboardButton(
            text=f'.{form.upper()}', callback_data=form) for form in formats_doc]

        for button in buttons:
            kb.insert(button)

        return kb
