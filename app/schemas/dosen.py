from pydantic import BaseModel, ConfigDict, Field


class DosenBase(BaseModel):
    nama: str = Field(min_length=1, max_length=255)
    kodeDosen: str = Field(min_length=1, max_length=255)


class DosenCreate(DosenBase):
    pass


class DosenUpdate(BaseModel):
    nama: str | None = Field(default=None, min_length=1, max_length=255)
    kodeDosen: str | None = Field(default=None, min_length=1, max_length=255)
    isDeleted: bool | None = None


class DosenRead(DosenBase):
    id: int
    isDeleted: bool

    model_config = ConfigDict(from_attributes=True)
