from fastapi import APIRouter

from app.api.routes.v1 import ping_endpoint
from app.api.routes.v1 import gif_search

router = APIRouter(prefix="/v1")

router.include_router(ping_endpoint.router, prefix="/ping")
router.include_router(gif_search.router, prefix="/gif_search")
