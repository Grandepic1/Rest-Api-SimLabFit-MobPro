from datetime import date, time

from pydantic import BaseModel, ConfigDict, Field


class KehadiranBase(BaseModel):
    idDosen: int
    idMataKuliah: int
    tanggal: date
    jamAwal: time
    jamAkhir: time
    ruangan: str = Field(min_length=1, max_length=255)
    modul: str = Field(min_length=1, max_length=255)
    kelas: str = Field(min_length=1, max_length=255)


class KehadiranCreate(KehadiranBase):
    googleId: str
    photoUrl: str | None = None


class KehadiranUpdate(BaseModel):
    idDosen: int | None = None
    idMataKuliah: int | None = None
    tanggal: date | None = None
    jamAwal: time | None = None
    jamAkhir: time | None = None
    ruangan: str | None = Field(default=None, min_length=1, max_length=255)
    modul: str | None = Field(default=None, min_length=1, max_length=255)
    kelas: str | None = Field(default=None, min_length=1, max_length=255)
    googleId: str | None = Field(default=None, min_length=1, max_length=255)
    photoUrl: str | None = Field(default=None, max_length=255)
    isDeleted: bool | None = None


class KehadiranRead(KehadiranBase):
    id: int
    googleId: str
    photoUrl: str | None
    isDeleted: bool

    model_config = ConfigDict(from_attributes=True)
