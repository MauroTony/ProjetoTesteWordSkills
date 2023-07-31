from sqlalchemy import Column, Integer, String, Boolean, inspect
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Hotels(Base):
    __tablename__ = "hotels"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), unique=True, index=True)
    sobre = Column(String(500))
    img_principal_base64 = Column(String(500))
    localizacaoLat = Column(String(255))
    localizacaoLong = Column(String(255))
    is_active = Column(Boolean, default=True)

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}


class Reservas(Base):
    __tablename__ = "reservas"

    id = Column(Integer, primary_key=True, index=True)
    id_hotel = Column(Integer, index=True)
    id_usuario = Column(Integer, index=True)
    data_inicio = Column(String(255))
    data_fim = Column(String(255))
    is_active = Column(Boolean, default=True)

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}


class GaleriaHotel(Base):
    __tablename__ = "galeria_hotel"

    id = Column(Integer, primary_key=True, index=True)
    id_hotel = Column(Integer, index=True)
    imagem_base64 = Column(String(500))

class Favoritos(Base):
    __tablename__ = "favoritos"

    id = Column(Integer, primary_key=True, index=True)
    id_hotel = Column(Integer, index=True)
    id_usuario = Column(Integer, index=True)
    is_active = Column(Boolean, default=True)
