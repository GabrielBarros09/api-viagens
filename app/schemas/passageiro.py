from pydantic import BaseModel

class PassageiroBase(BaseModel):
    id_usuario: int
    media_avaliacao: float

class PassageiroCreate(PassageiroBase):
    pass

class PassageiroResponse(PassageiroBase):
    id_passageiro: int

    class Config:
        from_attributes = True