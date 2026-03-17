from pydantic import BaseModel
from datetime import datetime

class CorridaBase(BaseModel):
    id_passageiro: int
    id_motorista: int
    id_servico: int
    id_avaliacao: int | None = None
    datahora_inicio: datetime
    datahora_fim: datetime | None = None
    local_partida: str
    local_destino: str
    valor_estimado: float
    status: str

class CorridaCreate(CorridaBase):
    pass

class CorridaResponse(CorridaBase):
    id_corrida: int

    class Config:
        from_attributes = True