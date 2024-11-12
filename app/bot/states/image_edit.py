from aiogram.fsm.state import State, StatesGroup


class ImageEditStateGroup(StatesGroup):
    get_photo = State()
    view_result = State()
