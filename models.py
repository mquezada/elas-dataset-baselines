from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class UDP(Base):
    __tablename__ = '__temp_Derechos_UDP'

    id = Column(Integer, primary_key=True)
    tipo = Column(String(255))
    id_interno = Column(Integer)
    pregunta = Column(Integer)
    valor = Column(String(255))
    categoria_id = Column(String(255))
    categoria = Column(Text)
    ela = Column(String(255))
    acuerdo = Column(String(255))
    region = Column(Integer)
    provincia = Column(Integer)
    comuna = Column(Integer)
    fundamento = Column(Text)
    pregunta_id = Column(String(255))
    normalizacion = Column(Text)
    modo = Column(String(255))
    sujeto = Column(Text)
    sintagma_v = Column(Text)
    sintagma_obj = Column(Text)
    comp = Column(Text)
    analista = Column(Text)