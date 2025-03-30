from fastapi import FastAPI

from core import events
from core.router import initialize_routes

app = FastAPI()



@app.on_event("startup")
async def startup() -> None:
    await events.startup_event_handler()


@app.on_event("shutdown")
async def shutdown_event() -> None:
    await events.shutdown_event_handler()


@app.get("/ping")
def read_root():
    return "pong!"


initialize_routes(app=app)
