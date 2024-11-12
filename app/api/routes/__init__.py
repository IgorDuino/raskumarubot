from configs.settings import env_parameters
from api.routes.v1 import router as v1_router
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

if env_parameters.IS_DEBUG:
    kwargs = {"debug": True}
else:
    kwargs = {"debug": False, "docs_url": None, "redoc_url": None, "openapi_url": None}

app = FastAPI(title="GenericTelegramBot backend", **kwargs)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)
app.include_router(v1_router, prefix="/api")

