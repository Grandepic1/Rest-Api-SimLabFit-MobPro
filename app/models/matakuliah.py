from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base
from app.models.dosen_matakuliah import dosen_matakuliah

if TYPE_CHECKING:
    from app.models.dosen import Dosen
    from app.models.kehadiran import Kehadiran


class Matakuliah(Base):
    __tablename__ = "matakuliah"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nama: Mapped[str] = mapped_column(String(255), nullable=False)
    kodeMataKuliah: Mapped[str] = mapped_column(String(255), nullable=False)
    isDeleted: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    dosens: Mapped[list["Dosen"]] = relationship(
        "Dosen",
        secondary=dosen_matakuliah,
        back_populates="matakuliahs",
    )
    kehadiran: Mapped[list["Kehadiran"]] = relationship(
        "Kehadiran",
        back_populates="matakuliah",
        cascade="all, delete-orphan",
    )