from fastapi import FastAPI, APIRouter

from apps.shortener.apis import shortener_router, stat_router

main_router = APIRouter()


def initialize_routes(app: FastAPI):
    app.include_router(main_router)
    app.include_router(shortener_router)
    app.include_router(stat_router)
