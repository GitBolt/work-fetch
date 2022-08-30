import requests
from fastapi import FastAPI
from bs4 import BeautifulSoup
import json
from boards import web3career
from boards import buildspace

app = FastAPI()
app.include_router(web3career.router)
app.include_router(buildspace.router)

@app.get('/')
async def root():
    return {"message": "hey! head over to /jobs"}

@app.on_event("startup")
async def startup() -> None:
    print("gm")

@app.on_event("shutdown")
async def shutdown() -> None:
    print("gn")