from core.constants.aspect_ratio import AspectRatio
from core.constants.styles import Style
from pydantic import BaseModel


class UserTextToImageSettings(BaseModel):
    style: Style = Style.NO_STYLE
    aspect_ratio: AspectRatio = AspectRatio.RATIO_16_9
    prompt: str = ""
    negative_prompt: str | None = None
