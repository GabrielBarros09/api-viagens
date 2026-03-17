from pydantic import BaseModel

class TipoCombustivelBase(BaseModel):
    descricao: str
    fator_carbono: float

class TipoCombustivelCreate(TipoCombustivelBase):
    pass

class TipoCombustivelResponse(TipoCombustivelBase):
    id_combustivel: int

    class Config:
        from_attributes = True