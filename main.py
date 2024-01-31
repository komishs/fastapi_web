from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# directory : 폴더 지정
templates = Jinja2Templates(directory="templates")

# @app.get("/")
@app.get("/", response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse(
        request = request, 
        name = "index.html",
        context = {
            "name" : 'hs'
        }
    )

@app.get("/hello")
async def hello():
    return "(fastapi) 안녕! 반가워!"