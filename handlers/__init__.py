from distutils.cmd import Command
from .user import *
from .admin import *

# DON'T TOUCH THIS IMPORT
from loader import dp


def setup(dp):
    """setup handlers for users and moders in one place and add throttling in 5 seconds

    Args:
        dp (Dispatcher): Dispatcher object
    """

    """user handlers"""
    dp.register_message_handler(
        cmd_start,
        commands=['start'],
        state=None)

    dp.register_message_handler(
        cmd_help,
        commands=['help'],
        state=None)

    """moder handlers"""
    dp.register_message_handler(
        cmd_info,
        commands=["info"],
        state=None)

    dp.register_message_handler(
        instagram_description,
        lambda message: 'www.instagram.com' in message.text.lower(),
        state=None)

    dp.register_message_handler(
        cmd_ocr,
        content_types=types.ContentTypes.PHOTO,
        state=None)

    dp.register_message_handler(
        cmd_convert,
        content_types=types.ContentTypes.DOCUMENT,
        state=None)

    dp.register_callback_query_handler(
        cmd_convert_ext,
        state=utils.fsm.choose_convert_ext.extention)
