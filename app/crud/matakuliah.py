from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.matakuliah import Matakuliah
from app.schemas.matakuliah import MatakuliahCreate, MatakuliahUpdate


async def get_matakuliah(db: AsyncSession, matakuliah_id: int) -> Matakuliah | None:
    result = await db.execute(
        select(Matakuliah).where(
            Matakuliah.id == matakuliah_id,
            Matakuliah.isDeleted.is_(False),
        )
    )
    return result.scalar_one_or_none()


async def list_matakuliah(db: AsyncSession) -> list[Matakuliah]:
    result = await db.execute(
        select(Matakuliah)
        .where(Matakuliah.isDeleted.is_(False))
        .order_by(Matakuliah.id)
    )
    return list(result.scalars().all())


async def create_matakuliah(
    db: AsyncSession,
    payload: MatakuliahCreate,
) -> Matakuliah:
    matakuliah = Matakuliah(**payload.model_dump())
    db.add(matakuliah)
    await db.commit()
    await db.refresh(matakuliah)
    return matakuliah


async def update_matakuliah(
    db: AsyncSession,
    matakuliah: Matakuliah,
    payload: MatakuliahUpdate,
) -> Matakuliah:
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(matakuliah, key, value)

    await db.commit()
    await db.refresh(matakuliah)
    return matakuliah


async def delete_matakuliah(db: AsyncSession, matakuliah: Matakuliah) -> None:
    matakuliah.isDeleted = True
    await db.commit()
