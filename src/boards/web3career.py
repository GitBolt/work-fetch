import requests
from fastapi import APIRouter
from bs4 import BeautifulSoup
import json
import time

router = APIRouter(prefix="/jobs")

@router.get('/web3career')
async def job():
    response = requests.get( "https://web3.career/solana-jobs?page=1")
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    results = soup.find_all("script")[0::2][1:-1]
    contents = [json.loads(result.text.replace("\n", "")) for result in results]
    print(contents)
    return contents