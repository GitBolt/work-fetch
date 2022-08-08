import requests
from fastapi import FastAPI
from bs4 import BeautifulSoup
import json


app = FastAPI()


@app.get('/')
async def root():
    return {"message": "hey! head over to /jobs"}

@app.get('/jobs')
async def job():
    response = requests.get("https://buildspace.so/jobs")
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    results = soup.find_all("script")
    parsed = json.loads(results[len(results)-1].text)
    jobs = parsed["props"]["pageProps"]["companies"]
    return jobs