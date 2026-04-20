from pydantic import BaseModel


class CatogoryBase(BaseModel):
    name: str


class CatogoryCreate(CatogoryBase):
    pass


class CatogoryResponse(CatogoryBase):
    id: int

    class Config:
        orm_mode = True
