from fastapi import FastAPI
from domain.users.routers import router as users_router
from domain.hotels.routers import router as hotels_router

app = FastAPI()

app.include_router(users_router, prefix="/users", tags=["users"])
app.include_router(hotels_router, tags=["hotels"])