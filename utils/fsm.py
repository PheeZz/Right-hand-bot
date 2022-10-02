"""Finite state machine classes module
    """

from aiogram.dispatcher.filters.state import State, StatesGroup


class choose_convert_ext(StatesGroup):
    extention = State()
    filename = State()
