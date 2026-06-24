from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import matakuliah as crud_matakuliah
from app.database.session import get_db
from app.schemas.matakuliah import MatakuliahCreate, MatakuliahRead, MatakuliahUpdate


router = APIRouter()


@router.get("/", response_model=list[MatakuliahRead])
async def list_matakuliah(db: AsyncSession = Depends(get_db)):
    return await crud_matakuliah.list_matakuliah(db)


@router.post("/", response_model=MatakuliahRead, status_code=status.HTTP_201_CREATED)
async def create_matakuliah(
    payload: MatakuliahCreate,
    db: AsyncSession = Depends(get_db),
):
    return await crud_matakuliah.create_matakuliah(db, payload)


@router.get("/{matakuliah_id}", response_model=MatakuliahRead)
async def get_matakuliah(matakuliah_id: int, db: AsyncSession = Depends(get_db)):
    matakuliah = await crud_matakuliah.get_matakuliah(db, matakuliah_id)
    if matakuliah is None:
        raise HTTPException(status_code=404, detail="Matakuliah not found")
    return matakuliah


@router.put("/{matakuliah_id}", response_model=MatakuliahRead)
async def update_matakuliah(
    matakuliah_id: int,
    payload: MatakuliahUpdate,
    db: AsyncSession = Depends(get_db),
):
    matakuliah = await crud_matakuliah.get_matakuliah(db, matakuliah_id)
    if matakuliah is None:
        raise HTTPException(status_code=404, detail="Matakuliah not found")
    return await crud_matakuliah.update_matakuliah(db, matakuliah, payload)


@router.delete("/{matakuliah_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_matakuliah(
    matakuliah_id: int,
    db: AsyncSession = Depends(get_db),
):
    matakuliah = await crud_matakuliah.get_matakuliah(db, matakuliah_id)
    if matakuliah is None:
        raise HTTPException(status_code=404, detail="Matakuliah not found")
    await crud_matakuliah.delete_matakuliah(db, matakuliah)
