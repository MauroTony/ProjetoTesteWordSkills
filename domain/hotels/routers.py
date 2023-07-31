from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .schemas import Hotel, ReservaCreate, GaleriaHotelCreate, FavoritoCreate, HotelBase,HotelCreate, ReservaBase
from .services import HotelService,ReservaService, GaleriaHotelService, FavoritoService
from .repositories import HotelRepository, ReservaRepository, GaleriaHotelRepository, FavoritoRepository
from .models import Hotels, Reservas, GaleriaHotel, Favoritos
from domain.users.models import User as UserModel
from dependencies import get_db
from dependencies import get_current_user

router = APIRouter()

@router.post("/hotels/", response_model=Hotel)
def create_hotel(hotel: HotelCreate, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="You don't have permission to create a hotel")
    hotel_service = HotelService(HotelRepository(db))
    try:
        response = hotel_service.create_hotel(hotel)
        return response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return

@router.get("/hotels/", response_model=List[HotelBase])
def read_hotels(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    hotel_service = HotelService(HotelRepository(db))
    hotels = hotel_service.get_hotels(skip=skip, limit=limit)
    return hotels

@router.delete("/hotels/{hotel_id}", response_model=HotelBase)
def delete_hotel(hotel_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="You don't have permission to delete a hotel")
    hotel_service = HotelService(HotelRepository(db))
    return hotel_service.delete_hotel(hotel_id)

@router.get("/reservas/")
def get_reservas(db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    reserva_repository = ReservaRepository(db)
    reserva_service = ReservaService(reserva_repository)
    return reserva_service.get_reservas(current_user)

@router.get("/datas_reservadas/{hotel_id}", response_model=List[ReservaBase])
def get_datas_reservadas(hotel_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    reserva_repository = ReservaRepository(db)
    reserva_service = ReservaService(reserva_repository)
    return reserva_service.get_datas_reservadas(hotel_id)

@router.post("/reservas/")
def create_reserva(reserva: ReservaCreate, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    reserva_repository = ReservaRepository(db)
    reserva_service = ReservaService(reserva_repository)
    return reserva_service.create_reserva(reserva, current_user)

@router.delete("/datas_reservadas/{reserva_id}")
def delete_reserva(reserva_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    reserva_repository = ReservaRepository(db)
    reserva_service = ReservaService(reserva_repository)
    reponse = reserva_service.delete_reserva(reserva_id, current_user)
    if not reponse:
        raise HTTPException(status_code=403, detail="You don't have permission to delete this reserva")
    return reponse

@router.get("/galeria/{hotel_id}")
def get_images(hotel_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    galeria_repository = GaleriaHotelRepository(db)
    galeria_service = GaleriaHotelService(galeria_repository)
    return galeria_service.get_images(hotel_id)

@router.post("/galeria/")
def create_image(image: GaleriaHotelCreate, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="You don't have permission to add a image")
    galeria_repository = GaleriaHotelRepository(db)
    galeria_service = GaleriaHotelService(galeria_repository)
    return galeria_service.create_image(image)

@router.delete("/galeria/{image_id}")
def delete_image(image_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="You don't have permission to delete a image")
    galeria_repository = GaleriaHotelRepository(db)
    galeria_service = GaleriaHotelService(galeria_repository)
    return galeria_service.delete_image(image_id)

@router.get("/favoritos/")
def get_favoritos(db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    favorito_repository = FavoritoRepository(db)
    favorito_service = FavoritoService(favorito_repository)
    return favorito_service.get_favoritos(current_user)

@router.post("/favoritos/")
def create_favorito(favorito: FavoritoCreate, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    favorito_repository = FavoritoRepository(db)
    favorito_service = FavoritoService(favorito_repository)
    return favorito_service.create_favorito(favorito, current_user)

@router.delete("/favoritos/{favorito_id}")
def delete_favorito(favorito_id: int, db: Session = Depends(get_db), current_user: UserModel = Depends(get_current_user)):
    favorito_repository = FavoritoRepository(db)
    favorito_service = FavoritoService(favorito_repository)
    response = favorito_service.delete_favorito(favorito_id, current_user)
    if not response:
        raise HTTPException(status_code=403, detail="You don't have permission to delete this favorito")
    return response