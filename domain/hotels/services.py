from .repositories import ReservaRepository, GaleriaHotelRepository, FavoritoRepository, HotelRepository
from .schemas import ReservaCreate, GaleriaHotelCreate, FavoritoCreate
from .models import Reservas, GaleriaHotel, Favoritos, Hotels

class HotelService:
    def __init__(self, hotel_repository: HotelRepository):
        self.hotel_repository = hotel_repository

    def create_hotel(self, hotel):
        return self.hotel_repository.create_hotel(hotel)

    def get_hotels(self, skip: int = 0, limit: int = 10):
        return self.hotel_repository.get_hotels(skip, limit)

    def delete_hotel(self, hotel_id: int):
        return self.hotel_repository.delete_hotel(hotel_id)

class ReservaService:
    def __init__(self, reserva_repository: ReservaRepository):
        self.reserva_repository = reserva_repository

    def get_reserva(self, reserva_id: int):
        return self.reserva_repository.get_reserva(reserva_id)

    def get_reservas(self, current_user):
        return self.reserva_repository.get_reservas(current_user)

    def get_datas_reservadas(self, hotel_id: int):
        return self.reserva_repository.get_datas_reservadas(hotel_id)
    def create_reserva(self, reserva: ReservaCreate, user):
        new_reserva = Reservas(**reserva.dict())
        new_reserva.id_usuario = user.id
        return self.reserva_repository.create_reserva(new_reserva)

    def delete_reserva(self, reserva_id: int, user):
        reserva = self.get_reserva(reserva_id)
        if reserva.id_usuario != user.id:
            return False
        return self.reserva_repository.delete_reserva(reserva_id)


class GaleriaHotelService:
    def __init__(self, galeria_hotel_repository: GaleriaHotelRepository):
        self.galeria_hotel_repository = galeria_hotel_repository

    def get_image(self, image_id: int):
        return self.galeria_hotel_repository.get_image(image_id)

    def get_images(self, hotel_id):
        return self.galeria_hotel_repository.get_images(hotel_id)

    def create_image(self, image: GaleriaHotelCreate):
        new_image = GaleriaHotel(**image.dict())
        return self.galeria_hotel_repository.create_image(new_image)

    def delete_image(self, image_id: int):
        return self.galeria_hotel_repository.delete_image(image_id)


class FavoritoService:
    def __init__(self, favorito_repository: FavoritoRepository):
        self.favorito_repository = favorito_repository

    def get_favorito(self, favorito_id: int):
        return self.favorito_repository.get_favorito(favorito_id)

    def get_favoritos(self, user):
        return self.favorito_repository.get_favoritos(user)

    def create_favorito(self, favorito: FavoritoCreate, user):
        new_favorito = Favoritos(**favorito.dict())
        new_favorito.id_usuario = user.id
        return self.favorito_repository.create_favorito(new_favorito)

    def delete_favorito(self, favorito_id: int, user):
        favorito = self.get_favorito(favorito_id)
        if favorito.id_usuario != user.id:
            return False
        return self.favorito_repository.delete_favorito(favorito_id)