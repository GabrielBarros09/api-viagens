from pydantic import BaseModel

class VeiculoBase(BaseModel):
    placa: str
    id_modelo: int
    tem_seguro: int
    id_classe: int

class VeiculoCreate(VeiculoBase):
    pass

class VeiculoResponse(VeiculoBase):
    id_veiculo: int

    class Config:
        from_attributes = True