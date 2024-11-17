"""
FastAPI application initialization and configuration.
Sets up CORS middleware and includes API routes.
Provides health check endpoint for monitoring application status.
"""

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.routes.health import router as health_router
from app.api.routes.v1 import router as v1_router
from app.api.routes.webhook import router as webhook_router
from app.bot import dp, setup_bot, stop_bot  # Import the dispatcher from your bot module
from app.core.configs.config import settings
from app.core.db import close_db, init_db
from app.core.logging import setup_logging

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging(level="DEBUG" if settings.IS_DEBUG else "INFO")
    await init_db()
    polling_task = await setup_bot(dp)

    yield

    await stop_bot(polling_task)
    await close_db()


if settings.IS_DEBUG:
    kwargs = {"debug": True}
else:
    kwargs = {"debug": False, "docs_url": None, "redoc_url": None, "openapi_url": None}
app = FastAPI(title="GenericTelegramBot backend", lifespan=lifespan, **kwargs)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)
app.include_router(health_router)
app.include_router(webhook_router)
app.include_router(v1_router, prefix="/api")
