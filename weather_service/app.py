from fastapi import FastAPI, APIRouter

from .endpoints import router


def create_app(routers: list[APIRouter]) -> FastAPI:
    new_app = FastAPI(
        root_path='/api/v1',
        title='Weather Service',
    )
    for r in routers:
        new_app.include_router(r)
    return new_app


app = create_app(routers=[router])
