from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import httpx
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

BASE_API = "https://cc-gen-api-production.up.railway.app"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    async with httpx.AsyncClient() as client:
        health = await client.get(f"{BASE_API}/health")
        health_data = health.json()
    return templates.TemplateResponse("index.html", {
        "request": request,
        "health": health_data
    })


@app.get("/bin-info", response_class=HTMLResponse)
async def bin_info(request: Request, bin: str = Query(...)):
    async with httpx.AsyncClient() as client:
        res = await client.get(f"{BASE_API}/bin/{bin}")
        if res.status_code != 200:
            return templates.TemplateResponse("index.html", {
                "request": request,
                "error": f"BIN info not found for {bin}",
                "health": {"status": "unknown"}
            })
        data = res.json()
    return templates.TemplateResponse("index.html", {
        "request": request,
        "bin_info": data,
        "health": {"status": "healthy"}
    })

@app.get("/generate")
async def redirect_generate(
    bin: str,
    limit: int = Query(default=None),
    month: str = Query(default=None),
    year: str = Query(default=None),
    cvv: str = Query(default=None)
):
    # Dynamically build query string
    params = [f"bin={bin}"]
    if limit is not None:
        params.append(f"limit={limit}")
    if month is not None:
        params.append(f"month={month}")
    if year is not None:
        params.append(f"year={year}")
    if cvv is not None:
        params.append(f"cvv={cvv}")
    
    query_string = "&".join(params)
    url = f"{BASE_API}/generate?{query_string}"
    return RedirectResponse(url)


@app.get("/generate/view")
async def redirect_txt(
    bin: str,
    limit: int = Query(default=None),
    month: str = Query(default=None),
    year: str = Query(default=None),
    cvv: str = Query(default=None)
):
    # Dynamically build query string
    params = [f"bin={bin}"]
    if limit is not None:
        params.append(f"limit={limit}")
    if month is not None:
        params.append(f"month={month}")
    if year is not None:
        params.append(f"year={year}")
    if cvv is not None:
        params.append(f"cvv={cvv}")
    
    query_string = "&".join(params)
    url = f"{BASE_API}/generate/view?{query_string}"
    return RedirectResponse(url)
