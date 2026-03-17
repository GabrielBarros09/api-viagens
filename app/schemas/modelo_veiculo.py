from pydantic import BaseModel

class ModeloVeiculoBase(BaseModel):
    nome_modelo: str
    cor: str
    fabricante: str
    ano: int
    capacidade: int
    propriedade: str
    id_combustivel: int

class ModeloVeiculoCreate(ModeloVeiculoBase):
    pass

class ModeloVeiculoResponse(ModeloVeiculoBase):
    id_modelo: int

    class Config:
        from_attributes = True