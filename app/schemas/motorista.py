from pydantic import BaseModel

class MotoristaBase(BaseModel):
    id_usuario: int
    media_avaliacao: float
    cnh: int

class MotoristaCreate(MotoristaBase):
    pass

class MotoristaResponse(MotoristaBase):
    id_motorista: int

    class Config:
        from_attributes = True