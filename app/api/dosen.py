from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import dosen as crud_dosen
from app.database.session import get_db
from app.schemas.dosen import DosenCreate, DosenRead, DosenUpdate


router = APIRouter()


@router.get("/", response_model=list[DosenRead])
async def list_dosen(db: AsyncSession = Depends(get_db)):
    return await crud_dosen.list_dosen(db)


@router.post("/", response_model=DosenRead, status_code=status.HTTP_201_CREATED)
async def create_dosen(payload: DosenCreate, db: AsyncSession = Depends(get_db)):
    return await crud_dosen.create_dosen(db, payload)


@router.get("/{dosen_id}", response_model=DosenRead)
async def get_dosen(dosen_id: int, db: AsyncSession = Depends(get_db)):
    dosen = await crud_dosen.get_dosen(db, dosen_id)
    if dosen is None:
        raise HTTPException(status_code=404, detail="Dosen not found")
    return dosen


@router.put("/{dosen_id}", response_model=DosenRead)
async def update_dosen(
    dosen_id: int,
    payload: DosenUpdate,
    db: AsyncSession = Depends(get_db),
):
    dosen = await crud_dosen.get_dosen(db, dosen_id)
    if dosen is None:
        raise HTTPException(status_code=404, detail="Dosen not found")
    return await crud_dosen.update_dosen(db, dosen, payload)


@router.delete("/{dosen_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_dosen(dosen_id: int, db: AsyncSession = Depends(get_db)):
    dosen = await crud_dosen.get_dosen(db, dosen_id)
    if dosen is None:
        raise HTTPException(status_code=404, detail="Dosen not found")
    await crud_dosen.delete_dosen(db, dosen)
