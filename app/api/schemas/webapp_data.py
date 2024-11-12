from core.constants.actions import ActionEnum
from core.routes.v1.schemas import CreateOutfitRequest, CreateUpscaleRequest
from pydantic import BaseModel


class WebappSendDataData(BaseModel):
    action: ActionEnum
    # allow empty dict as data as one of the options
    data: CreateOutfitRequest | CreateUpscaleRequest | None
