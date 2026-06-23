from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base
from app.models.dosen_matakuliah import dosen_matakuliah

if TYPE_CHECKING:
    from app.models.kehadiran import Kehadiran
    from app.models.matakuliah import Matakuliah


class Dosen(Base):
    __tablename__ = "dosen"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nama: Mapped[str] = mapped_column(String(255), nullable=False)
    kodeDosen: Mapped[str] = mapped_column(String(255), nullable=False)
    isDeleted: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    matakuliahs: Mapped[list["Matakuliah"]] = relationship(
        "Matakuliah",
        secondary=dosen_matakuliah,
        back_populates="dosens",
    )

    kehadiran: Mapped[list["Kehadiran"]] = relationship(
        "Kehadiran",
        back_populates="dosen",
        cascade="all, delete-orphan",
    )