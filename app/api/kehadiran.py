from datetime import date, time
from pathlib import Path
from uuid import uuid4

from fastapi import APIRouter, Depends, File, Form, Header, HTTPException, UploadFile, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import dosen as crud_dosen
from app.crud import kehadiran as crud_kehadiran
from app.crud import matakuliah as crud_matakuliah
from app.database.session import get_db
from app.schemas.kehadiran import KehadiranCreate, KehadiranRead, KehadiranUpdate


router = APIRouter()
UPLOAD_DIR = Path("app/static/uploads/kehadiran")


async def save_image(file: UploadFile | None) -> str | None:
    if file is None:
        return None
    if file.content_type is None or not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Uploaded file must be an image")

    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    extension = Path(file.filename or "").suffix
    filename = f"{uuid4().hex}{extension}"
    file_path = UPLOAD_DIR / filename
    file_path.write_bytes(await file.read())
    return f"/static/uploads/kehadiran/{filename}"


@router.get("/", response_model=list[KehadiranRead])
async def list_kehadiran(
    authorization: str = Header(...),
    db: AsyncSession = Depends(get_db),
):
    return await crud_kehadiran.list_kehadiran(db, google_id=authorization)


@router.post("/", response_model=KehadiranRead, status_code=status.HTTP_201_CREATED)
async def create_kehadiran(
    idDosen: int = Form(...),
    idMataKuliah: int = Form(...),
    tanggal: date = Form(...),
    jamAwal: time = Form(...),
    jamAkhir: time = Form(...),
    ruangan: str = Form(..., min_length=1, max_length=255),
    modul: str = Form(..., min_length=1, max_length=255),
    kelas: str = Form(..., min_length=1, max_length=255),
    image: UploadFile | None = File(default=None),
    authorization: str = Header(...),
    db: AsyncSession = Depends(get_db),
):
    dosen = await crud_dosen.get_dosen(db, idDosen)
    matakuliah = await crud_matakuliah.get_matakuliah(db, idMataKuliah)
    if dosen is None or matakuliah is None:
        raise HTTPException(status_code=404, detail="Dosen or matakuliah not found")

    photo_url = await save_image(image)
    payload = KehadiranCreate(
        idDosen=idDosen,
        idMataKuliah=idMataKuliah,
        tanggal=tanggal,
        jamAwal=jamAwal,
        jamAkhir=jamAkhir,
        ruangan=ruangan,
        modul=modul,
        kelas=kelas,
        googleId=authorization,
        photoUrl=photo_url,
    )
    return await crud_kehadiran.create_kehadiran(db, payload)


@router.get("/{kehadiran_id}", response_model=KehadiranRead)
async def get_kehadiran(
    kehadiran_id: int,
    authorization: str = Header(...),
    db: AsyncSession = Depends(get_db),
):
    kehadiran = await crud_kehadiran.get_kehadiran(
        db,
        kehadiran_id,
        google_id=authorization,
    )
    if kehadiran is None:
        raise HTTPException(status_code=404, detail="Kehadiran not found")
    return kehadiran


@router.put("/{kehadiran_id}", response_model=KehadiranRead)
async def update_kehadiran(
    kehadiran_id: int,
    idDosen: int = Form(...),
    idMataKuliah: int = Form(...),
    tanggal: date = Form(...),
    jamAwal: time = Form(...),
    jamAkhir: time = Form(...),
    ruangan: str = Form(..., min_length=1, max_length=255),
    modul: str = Form(..., min_length=1, max_length=255),
    kelas: str = Form(..., min_length=1, max_length=255),
    image: UploadFile | None = File(default=None),
    authorization: str = Header(...),
    db: AsyncSession = Depends(get_db),
):
    kehadiran = await crud_kehadiran.get_kehadiran(
        db,
        kehadiran_id,
        google_id=authorization,
    )
    if kehadiran is None:
        raise HTTPException(status_code=404, detail="Kehadiran not found")

    dosen = await crud_dosen.get_dosen(db, idDosen)
    matakuliah = await crud_matakuliah.get_matakuliah(db, idMataKuliah)
    if dosen is None or matakuliah is None:
        raise HTTPException(status_code=404, detail="Dosen or matakuliah not found")

    payload_data = {
        "idDosen": idDosen,
        "idMataKuliah": idMataKuliah,
        "tanggal": tanggal,
        "jamAwal": jamAwal,
        "jamAkhir": jamAkhir,
        "ruangan": ruangan,
        "modul": modul,
        "kelas": kelas,
        "googleId": authorization,
    }
    photo_url = await save_image(image)
    if photo_url is not None:
        payload_data["photoUrl"] = photo_url

    payload = KehadiranUpdate(**payload_data)
    return await crud_kehadiran.update_kehadiran(db, kehadiran, payload)


@router.delete("/{kehadiran_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_kehadiran(
    kehadiran_id: int,
    authorization: str = Header(...),
    db: AsyncSession = Depends(get_db),
):
    kehadiran = await crud_kehadiran.get_kehadiran(
        db,
        kehadiran_id,
        google_id=authorization,
    )
    if kehadiran is None:
        raise HTTPException(status_code=404, detail="Kehadiran not found")
    await crud_kehadiran.delete_kehadiran(db, kehadiran)
