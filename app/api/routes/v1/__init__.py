from api.routes.v1 import (
    generation_endpoints,
    refresh_url_endpoints,
    settings_endpoints,
)
from app.api.routes.v1 import ping_endpoint
from fastapi import APIRouter

router = APIRouter(prefix="/v1")

router.include_router(ping_endpoint.router, prefix="/ping")
