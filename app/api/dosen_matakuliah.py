from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import dosen as crud_dosen
from app.crud import dosen_matakuliah as crud_dosen_matakuliah
from app.crud import matakuliah as crud_matakuliah
from app.database.session import get_db
from app.schemas.dosen_matakuliah import DosenMatakuliahCreate, DosenMatakuliahRead


router = APIRouter()


@router.get("/", response_model=list[DosenMatakuliahRead])
async def list_dosen_matakuliah(db: AsyncSession = Depends(get_db)):
    return await crud_dosen_matakuliah.list_dosen_matakuliah(db)


@router.post(
    "/",
    response_model=DosenMatakuliahRead,
    status_code=status.HTTP_201_CREATED,
)
async def create_dosen_matakuliah(
    payload: DosenMatakuliahCreate,
    db: AsyncSession = Depends(get_db),
):
    dosen = await crud_dosen.get_dosen(db, payload.idDosen)
    matakuliah = await crud_matakuliah.get_matakuliah(db, payload.idMataKuliah)
    if dosen is None or matakuliah is None:
        raise HTTPException(
            status_code=404,
            detail="Dosen or matakuliah not found",
        )

    try:
        return await crud_dosen_matakuliah.create_dosen_matakuliah(db, payload)
    except IntegrityError as exc:
        await db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Dosen matakuliah already exists",
        ) from exc


@router.delete(
    "/{id_dosen}/{id_matakuliah}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_dosen_matakuliah(
    id_dosen: int,
    id_matakuliah: int,
    db: AsyncSession = Depends(get_db),
):
    relation = await crud_dosen_matakuliah.get_dosen_matakuliah(
        db,
        id_dosen,
        id_matakuliah,
    )
    if relation is None:
        raise HTTPException(status_code=404, detail="Dosen matakuliah not found")
    await crud_dosen_matakuliah.delete_dosen_matakuliah(db, id_dosen, id_matakuliah)
