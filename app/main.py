from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routers import predict

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(predict.router)

templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})
