from fastapi import FastAPI
from src.infrastructure.database.connection import engine, Base
from src.api.routes import router


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Contracs Predictor Model")
app.include_router(router) 