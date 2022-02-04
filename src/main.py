from fastapi import FastAPI
from time import time_ns
from datetime import datetime

app = FastAPI()


@app.get("/")
async def root():
    return {"@timestamp": datetime.now(), "datetime": time_ns()}
