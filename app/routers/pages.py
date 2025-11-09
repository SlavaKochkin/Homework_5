from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
import os

router = APIRouter()


project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
templates_dir = os.path.join(project_root, "templates")
templates = Jinja2Templates(directory=templates_dir)


@router.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "Главная страница"})


@router.get("/about/")
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request, "title": "О нас"})

