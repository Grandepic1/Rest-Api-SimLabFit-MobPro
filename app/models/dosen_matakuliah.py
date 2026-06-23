from sqlalchemy import Column, ForeignKey, Index, Integer, Table

from app.database.base import Base


dosen_matakuliah = Table(
    "dosen_matakuliah",
    Base.metadata,
    Column(
        "idDosen",
        Integer,
        ForeignKey("dosen.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column(
        "idMataKuliah",
        Integer,
        ForeignKey("matakuliah.id", ondelete="CASCADE"),
        primary_key=True,
    ),
)

Index("ix_dosen_matakuliah_idDosen", dosen_matakuliah.c.idDosen)
Index("ix_dosen_matakuliah_idMataKuliah", dosen_matakuliah.c.idMataKuliah)
