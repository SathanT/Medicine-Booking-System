from fastapi import APIRouter

from api.routes import (
    address_route,
    catogory_route,
    manufactuerer_route,
    medicine_route,
    order_route,
    user_route,
)

api_router = APIRouter()

api_router.include_router(address_route.router)
api_router.include_router(catogory_route.router)
api_router.include_router(manufactuerer_route.router)
api_router.include_router(medicine_route.router)
api_router.include_router(order_route.router)
api_router.include_router(user_route.router)
