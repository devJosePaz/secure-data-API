from fastapi import FastAPI
from app.routes.transaction_routes import router

app = FastAPI()

app.include_router(router)