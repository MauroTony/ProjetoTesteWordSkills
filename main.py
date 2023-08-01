from fastapi import FastAPI
from domain.users.routers import router as users_router
from domain.hotels.routers import router as hotels_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router, prefix="/users", tags=["users"])
app.include_router(hotels_router, tags=["hotels"])