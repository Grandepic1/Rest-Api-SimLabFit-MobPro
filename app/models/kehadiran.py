from __future__ import annotations

from datetime import date, time
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Date, ForeignKey, String, Time
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base

if TYPE_CHECKING:
    from app.models.dosen import Dosen
    from app.models.matakuliah import Matakuliah


class Kehadiran(Base):
    __tablename__ = "kehadiran"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    idDosen: Mapped[int] = mapped_column(
        ForeignKey("dosen.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    idMataKuliah: Mapped[int] = mapped_column(
        ForeignKey("matakuliah.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    tanggal: Mapped[date] = mapped_column(Date, nullable=False)
    jamAwal: Mapped[time] = mapped_column(Time, nullable=False)
    jamAkhir: Mapped[time] = mapped_column(Time, nullable=False)
    ruangan: Mapped[str] = mapped_column(String(255), nullable=False)
    modul: Mapped[str] = mapped_column(String(255), nullable=False)
    kelas: Mapped[str] = mapped_column(String(255), nullable=False)
    isDeleted: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    dosen: Mapped["Dosen"] = relationship("Dosen", back_populates="kehadiran")
    matakuliah: Mapped["Matakuliah"] = relationship(
        "Matakuliah",
        back_populates="kehadiran",
    )