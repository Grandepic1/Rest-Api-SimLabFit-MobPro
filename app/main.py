from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.items import router as items_router
from app.core.config import settings


app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG,
)

app.include_router(health_router)
app.include_router(items_router, prefix="/items", tags=["items"])


@app.get("/")
async def root():
    return {
        "message": "Sample REST API",
        "docs": "/docs",
        "health": "/health",
    }
