from sqlalchemy import Column, BigInteger, SmallInteger, DateTime
from app.database import Base

class AvaliacaoModel(Base):
    __tablename__ = "avaliacao"

    id_avaliacao = Column(BigInteger, primary_key=True, autoincrement=True)
    nota_passageiro = Column(SmallInteger)
    nota_motorista = Column(SmallInteger)
    datahora_inicio = Column(DateTime)