from pydantic import BaseModel
from typing import Optional
class HotelBase(BaseModel):
    id: Optional[int] = None
    nome: Optional[str] = None
    sobre: Optional[str] = None
    localizacaoLat: Optional[str] = None
    localizacaoLong: Optional[str] = None
    img_principal_base64: Optional[str] = True

    class Config:
        from_attributes = True

class HotelCreate(HotelBase):
    nome: str
    sobre: str
    localizacaoLat: str
    localizacaoLong: str
    img_principal_base64: str

class Hotel(HotelBase):
    id: int

    class Config:
        orm_mode = True

class ReservaBase(BaseModel):
    id_hotel: int
    data_inicio: str
    data_fim: str

class ReservaCreate(ReservaBase):
    pass

class Reserva(ReservaBase):
    id: int

    class Config:
        from_attributes = True

class GaleriaHotelBase(BaseModel):
    id_hotel: int
    imagem_base64: str

class GaleriaHotelCreate(GaleriaHotelBase):
    pass

class GaleriaHotel(GaleriaHotelBase):
    id: int

    class Config:
        from_attributes = True

class FavoritoBase(BaseModel):
    id_hotel: int

class FavoritoCreate(FavoritoBase):
    pass

class Favorito(FavoritoBase):
    id: int

    class Config:
        from_attributes = True