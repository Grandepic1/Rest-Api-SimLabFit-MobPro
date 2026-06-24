from pydantic import BaseModel, ConfigDict


class DosenMatakuliahCreate(BaseModel):
    idDosen: int
    idMataKuliah: int


class DosenMatakuliahRead(DosenMatakuliahCreate):
    model_config = ConfigDict(from_attributes=True)
