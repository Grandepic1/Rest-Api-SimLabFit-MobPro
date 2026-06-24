from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.dosen import router as dosen_router
from app.api.dosen_matakuliah import router as dosen_matakuliah_router
from app.api.health import router as health_router
from app.api.items import router as items_router
from app.api.kehadiran import router as kehadiran_router
from app.api.matakuliah import router as matakuliah_router
from app.core.config import settings


app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG,
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(health_router)
app.include_router(items_router, prefix="/items", tags=["items"])
app.include_router(dosen_router, prefix="/dosen", tags=["dosen"])
app.include_router(matakuliah_router, prefix="/matakuliah", tags=["matakuliah"])
app.include_router(
    dosen_matakuliah_router,
    prefix="/dosen-matakuliah",
    tags=["dosen-matakuliah"],
)
app.include_router(kehadiran_router, prefix="/kehadiran", tags=["kehadiran"])


@app.get("/")
async def root():
    return {
        "message": "Sample REST API",
        "docs": "/docs",
        "health": "/health",
    }
