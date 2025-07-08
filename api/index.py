from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import httpx
import random
import os

app = FastAPI()
BASE_URL = "https://cc-gen-api-production.up.railway.app"

# Templates and static files
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="static")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("style.css", {"request": request})

@app.get("/generate")
async def generate(
    bin: str = Query(...),
    limit: int = Query(10),
    month: str = Query(...),
    year: str = Query(...),
    cvv: str = Query(None),
    format: str = Query("json")  # or 'txt'
):
    if not cvv:
        cvv = "".join([str(random.randint(0, 9)) for _ in range(3)])
    url = f"{BASE_URL}/generate"
    params = {"bin": bin, "limit": limit, "month": month, "year": year, "cvv": cvv}

    async with httpx.AsyncClient() as client:
        if format == "txt":
            view_url = f"{BASE_URL}/generate/view"
            r = await client.get(view_url, params=params)
            return PlainTextResponse(content=r.text)
        else:
            r = await client.get(url, params=params)
            return r.json()

@app.get("/bin/{bin_number}")
async def get_bin_info(bin_number: str):
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{BASE_URL}/bin/{bin_number}")
        return r.json()

@app.get("/health")
async def health():
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{BASE_URL}/health")
        return r.json()
