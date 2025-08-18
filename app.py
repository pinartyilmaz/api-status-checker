from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl
import aiohttp
import asyncio
from typing import List


app = FastAPI()

class status_request(BaseModel):
    urls: list[str]

class status_response(BaseModel):
    url: str
    status: int

@app.post("/status", response_model=List[status_response])
async def check_urls(request: status_request):
    async with aiohttp.ClientSession() as session:
        tasks = [status_checker(url=url, session=session) for url in request.urls]
        results = await asyncio.gather(*tasks)
    return results

async def status_checker(url: str, session: aiohttp.ClientSession):
    try:
        async with session.get(url) as response:
            return status_response(url=url, status=response.status)
    except aiohttp.ClientError as e:
        return status_response(url=url, status=500)



