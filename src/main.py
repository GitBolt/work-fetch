import requests
from fastapi import FastAPI
from bs4 import BeautifulSoup

app = FastAPI()


@app.get('/')
async def root():
    return {"message": "hey! head over to /jobs"}

@app.get('/jobs')
async def job():
    response = requests.get("https://buildspace.so/jobs")
    html = response.text
    soup = BeautifulSoup(html)
    results = soup.find_all("p", class_="chakra-text")
    print(results)