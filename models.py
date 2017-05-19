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


class PNUD(Base):
    __tablename__ = 'data_conceptos_tareas_PNUD'

    id = Column(Integer, primary_key=True)
    id_ela = Column(String(255), primary_key=True)
    tema = Column(Integer)
    categoria = Column(Text)
    pnud = Column(Integer)
    concepto_original = Column(Text)
    fundamento = Column(Text)
    modo = Column(String(255))

    def __repr__(self):
        return f"<id=({self.id}, " \
               f"{self.id_ela}), " \
               f"tema={self.tema}, " \
               f"pnud={self.pnud}, " \
               f"concepto_orig='{self.concepto_original}'>"