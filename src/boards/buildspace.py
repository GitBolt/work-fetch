import requests
from fastapi import APIRouter
from bs4 import BeautifulSoup
import json

router = APIRouter(prefix="/jobs")

@router.get('/buildspace')
async def job():
    response = requests.get("https://buildspace.so/jobs")
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    results = soup.find_all("script")
    parsed = json.loads(results[len(results)-1].text)
    jobs = parsed["props"]["pageProps"]["companies"]
    return jobs