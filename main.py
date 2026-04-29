from fastapi import FastAPI


from api.router import api_router
from db.init_db import init_db

init_db()
app = FastAPI()

app.include_router(api_router)