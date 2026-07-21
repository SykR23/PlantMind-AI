from fastapi import FastAPI
from api.routes import router
from config.config import config

app = FastAPI(
    title="PlantMind API",
    description=config.APP_DESCRIPTION,
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.include_router(router)