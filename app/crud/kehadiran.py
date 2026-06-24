from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.kehadiran import Kehadiran
from app.schemas.kehadiran import KehadiranCreate, KehadiranUpdate


async def get_kehadiran(
    db: AsyncSession,
    kehadiran_id: int,
    google_id: str | None = None,
) -> Kehadiran | None:
    query = select(Kehadiran).where(
        Kehadiran.id == kehadiran_id,
        Kehadiran.isDeleted.is_(False),
    )
    if google_id is not None:
        query = query.where(Kehadiran.googleId == google_id)

    result = await db.execute(query)
    return result.scalar_one_or_none()


async def list_kehadiran(db: AsyncSession, google_id: str | None = None) -> list[Kehadiran]:
    query = select(Kehadiran).where(Kehadiran.isDeleted.is_(False))
    if google_id is not None:
        query = query.where(Kehadiran.googleId == google_id)

    result = await db.execute(query.order_by(Kehadiran.id))
    return list(result.scalars().all())


async def create_kehadiran(
    db: AsyncSession,
    payload: KehadiranCreate,
) -> Kehadiran:
    kehadiran = Kehadiran(**payload.model_dump())
    db.add(kehadiran)
    await db.commit()
    await db.refresh(kehadiran)
    return kehadiran


async def update_kehadiran(
    db: AsyncSession,
    kehadiran: Kehadiran,
    payload: KehadiranUpdate,
) -> Kehadiran:
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(kehadiran, key, value)

    await db.commit()
    await db.refresh(kehadiran)
    return kehadiran


async def delete_kehadiran(db: AsyncSession, kehadiran: Kehadiran) -> None:
    kehadiran.isDeleted = True
    await db.commit()
