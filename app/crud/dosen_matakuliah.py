from sqlalchemy import delete, insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.dosen_matakuliah import dosen_matakuliah
from app.schemas.dosen_matakuliah import DosenMatakuliahCreate


async def list_dosen_matakuliah(db: AsyncSession) -> list[dict[str, int]]:
    result = await db.execute(
        select(
            dosen_matakuliah.c.idDosen,
            dosen_matakuliah.c.idMataKuliah,
        ).order_by(dosen_matakuliah.c.idDosen, dosen_matakuliah.c.idMataKuliah)
    )
    return [dict(row._mapping) for row in result.all()]


async def get_dosen_matakuliah(
    db: AsyncSession,
    id_dosen: int,
    id_matakuliah: int,
) -> dict[str, int] | None:
    result = await db.execute(
        select(
            dosen_matakuliah.c.idDosen,
            dosen_matakuliah.c.idMataKuliah,
        ).where(
            dosen_matakuliah.c.idDosen == id_dosen,
            dosen_matakuliah.c.idMataKuliah == id_matakuliah,
        )
    )
    row = result.first()
    return dict(row._mapping) if row else None


async def create_dosen_matakuliah(
    db: AsyncSession,
    payload: DosenMatakuliahCreate,
) -> dict[str, int]:
    await db.execute(insert(dosen_matakuliah).values(**payload.model_dump()))
    await db.commit()
    return payload.model_dump()


async def delete_dosen_matakuliah(
    db: AsyncSession,
    id_dosen: int,
    id_matakuliah: int,
) -> None:
    await db.execute(
        delete(dosen_matakuliah).where(
            dosen_matakuliah.c.idDosen == id_dosen,
            dosen_matakuliah.c.idMataKuliah == id_matakuliah,
        )
    )
    await db.commit()
