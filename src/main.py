from fastapi import FastAPI
from time import time, time_ns

app = FastAPI()


@app.get("/")
async def root():
    return {"@timestamp": time_ns()}
