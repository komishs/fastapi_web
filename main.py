from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# directory : 폴더 지정
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse(
        request = request, 
        name = "index.html",
        context = {
            "name" : 'hs'
        }
    )

# pass parameters
@app.get('/hello/{name}', response_class=HTMLResponse)
async def hello(
    request: Request , name , action, sound: str = '빵빵'
):
    print(f'action :{action} 그리고 소리 :{sound} ')
    return templates.TemplateResponse(
        request=request,
        name="hello.html" , 
        context={
            "name"   : name,
            "action" : action,
            'sound'  : sound
        }
    )

@app.get('/login', response_class=HTMLResponse)
async def login_page_view(request: Request):
    return templates.TemplateResponse(
        request = request,
        name='login.html'
    )

@app.post('/login', response_class=HTMLResponse)
async def login(username: str=Form(...), password:str=Form(...)):
    print(username, password)
    return f"Success, {username}님"
    # return "Success"

@app.get('/register', response_class=HTMLResponse)
async def register_page_view(request: Request):
    return templates.TemplateResponse(
        request = request,
        name='register.html'
    )

@app.post('/register', response_class=HTMLResponse)
async def register(
    username: str=Form(...), 
    email: str=Form(...),
    phone: str=Form(...),
    password:str=Form(...)
):
    print(username, email, phone, password)
    return f"Success, {username}님"