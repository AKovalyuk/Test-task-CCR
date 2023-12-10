from fastapi import FastAPI, APIRouter

from .endpoints import router


def create_app(routers: list[APIRouter]) -> FastAPI:
    new_app = FastAPI(
        title='Weather Service',
    )
    for r in routers:
        new_app.include_router(r)
    return new_app


app = create_app(routers=[router])
