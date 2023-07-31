from sqlalchemy.orm import Session
from .models import Hotels, Reservas, GaleriaHotel, Favoritos
from sqlalchemy import or_, select
from .schemas import HotelBase
class HotelRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_hotel(self, hotel_id: int):
        return self.db.query(Hotels).filter(Hotels.id == hotel_id).first()

    def get_hotels(self, skip: int = 0, limit: int = 10):
        return self.db.query(Hotels).offset(skip).limit(limit).all()

    def create_hotel(self, hotel):
        db_hotel = Hotels(**hotel.dict())
        self.db.add(db_hotel)
        self.db.commit()
        return db_hotel

    def delete_hotel(self, hotel_id: int):
        db_hotel = self.db.query(Hotels).filter(Hotels.id == hotel_id).first()
        self.db.delete(db_hotel)
        self.db.commit()
        return db_hotel

class ReservaRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_reserva(self, reserva_id: int):
        return self.db.query(Reservas).filter(Reservas.id == reserva_id).first()

    def get_reservas(self, current_user):
        query = select(Reservas, Hotels). \
            join(Hotels, Reservas.id_hotel == Hotels.id). \
            where(Reservas.id_usuario == current_user.id)
        # execute a consulta
        results = self.db.execute(query)
        # retorna as reservas e os hotéis como uma lista de tuplas (Reservas, Hotels)
        reservations_hotels = [{"reserva": reservation.to_dict(), "hotel": hotel.to_dict()}
                               for reservation, hotel in results]
        return reservations_hotels # self.db.query(Reservas).all()

    def get_datas_reservadas(self, hotel_id):
        return self.db.query(Reservas).filter(Reservas.id_hotel == hotel_id).all()

    def create_reserva(self, reserva):
        self.db.add(reserva)
        self.db.commit()
        self.db.refresh(reserva)
        return reserva

    def delete_reserva(self, reserva_id: int):
        reserva = self.get_reserva(reserva_id)
        if reserva:
            self.db.delete(reserva)
            self.db.commit()
            return True
        return False

class GaleriaHotelRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_image(self, image_id: int):
        return self.db.query(GaleriaHotel).filter(GaleriaHotel.id == image_id).first()

    def get_images(self, hotel_id):
        return self.db.query(GaleriaHotel).filter(GaleriaHotel.id_hotel == hotel_id).all()

    def create_image(self, image):
        self.db.add(image)
        self.db.commit()
        self.db.refresh(image)
        return image

    def delete_image(self, image_id: int):
        image = self.get_image(image_id)
        if image:
            self.db.delete(image)
            self.db.commit()
            return True
        return False

class FavoritoRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_favorito(self, favorito_id: int):
        return self.db.query(Favoritos).filter(Favoritos.id == favorito_id).first()

    def get_favoritos(self, user):
        fav_hotels_ids = select(Favoritos.id_hotel).where(Favoritos.id_usuario == user.id)
        hotels_query = select(Hotels).where(Hotels.id.in_(fav_hotels_ids))
        results = self.db.execute(hotels_query)
        hotels = results.scalars().all()
        return hotels # self.db.query(Favoritos).filter(Favoritos.id_usuario == user.id).all()

    def create_favorito(self, favorito):
        self.db.add(favorito)
        self.db.commit()
        self.db.refresh(favorito)
        return favorito

    def delete_favorito(self, favorito_id: int):
        favorito = self.get_favorito(favorito_id)
        if favorito:
            self.db.delete(favorito)
            self.db.commit()
            return True
        return False