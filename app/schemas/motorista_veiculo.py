from pydantic import BaseModel
from datetime import datetime

class MotoristaVeiculoBase(BaseModel):
    id_motorista: int
    id_veiculo: int
    datahora_inicio: datetime
    datahora_fim: datetime | None = None

class MotoristaVeiculoCreate(MotoristaVeiculoBase):
    pass

class MotoristaVeiculoResponse(MotoristaVeiculoBase):
    class Config:
        from_attributes = True