from aiogram.fsm.state import State, StatesGroup


class ImageToTextStateGroup(StatesGroup):
    get_prompt = State()
    view_result = State()
    generate_image_to_text = State()
