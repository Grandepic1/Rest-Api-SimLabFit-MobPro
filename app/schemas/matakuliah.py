from pydantic import BaseModel, ConfigDict, Field


class MatakuliahBase(BaseModel):
    nama: str = Field(min_length=1, max_length=255)
    kodeMataKuliah: str = Field(min_length=1, max_length=255)


class MatakuliahCreate(MatakuliahBase):
    pass


class MatakuliahUpdate(BaseModel):
    nama: str | None = Field(default=None, min_length=1, max_length=255)
    kodeMataKuliah: str | None = Field(default=None, min_length=1, max_length=255)
    isDeleted: bool | None = None


class MatakuliahRead(MatakuliahBase):
    id: int
    isDeleted: bool

    model_config = ConfigDict(from_attributes=True)
