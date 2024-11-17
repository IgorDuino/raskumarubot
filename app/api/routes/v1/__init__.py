from fastapi import APIRouter

from app.api.routes.v1 import ping_endpoint

router = APIRouter(prefix="/v1")

router.include_router(ping_endpoint.router, prefix="/ping")
