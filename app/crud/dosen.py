from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.dosen import Dosen
from app.schemas.dosen import DosenCreate, DosenUpdate


async def get_dosen(db: AsyncSession, dosen_id: int) -> Dosen | None:
    result = await db.execute(
        select(Dosen).where(Dosen.id == dosen_id, Dosen.isDeleted.is_(False))
    )
    return result.scalar_one_or_none()


async def list_dosen(db: AsyncSession) -> list[Dosen]:
    result = await db.execute(
        select(Dosen).where(Dosen.isDeleted.is_(False)).order_by(Dosen.id)
    )
    return list(result.scalars().all())


async def create_dosen(db: AsyncSession, payload: DosenCreate) -> Dosen:
    dosen = Dosen(**payload.model_dump())
    db.add(dosen)
    await db.commit()
    await db.refresh(dosen)
    return dosen


async def update_dosen(
    db: AsyncSession,
    dosen: Dosen,
    payload: DosenUpdate,
) -> Dosen:
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(dosen, key, value)

    await db.commit()
    await db.refresh(dosen)
    return dosen


async def delete_dosen(db: AsyncSession, dosen: Dosen) -> None:
    dosen.isDeleted = True
    await db.commit()
