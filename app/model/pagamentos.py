from sqlalchemy import Column, BigInteger, DECIMAL, DateTime, SmallInteger, ForeignKey
from app.database import Base

class PagamentoModel(Base):
    __tablename__ = "pagamentos"

    id_pagamento = Column(BigInteger, primary_key=True, autoincrement=True)
    id_corrida = Column(BigInteger, ForeignKey("corrida.id_corrida"))
    valor = Column(DECIMAL(10,2))
    id_metodo_pagamento = Column(SmallInteger, ForeignKey("metodo_pagamento.id_metodo_pagamento"))
    datahora_transacao = Column(DateTime)