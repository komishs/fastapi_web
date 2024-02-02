from pymongo import MongoClient


from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from fastapi.responses import RedirectResponse

from passlib.hash import pbkdf2_sha256
# password를 hash code로 변환

app = FastAPI()

# mongodb connect
mongodb_URI = "mongodb+srv://root:1234@ubion9.f9lapgm.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(mongodb_URI)
db = client.ubion9 # 공통 database

# directory : 폴더 지정
templates = Jinja2Templates(directory="templates")
salt = "ubion"

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
async def login(request : Request, email: str=Form(...), password:str=Form(...)):
    # print(username, password)
    user = db.users.find_one({'email' : email})
    if user == None:
        # 가입정보가 없음 -> 회원가입 페이지로 이동
        return templates.TemplateResponse(
            request = request,
            name='register.html'
        )
    else:
        pwd = user['password']
        result = pbkdf2_sha256.verify(password + salt, pwd)
        if result:
            # 로그인 성공 -> index 페이지로 이동
            return templates.TemplateResponse(
                request = request, 
                name = "index.html",
                context = {
                    "name" : email
            })
        else:
            # 로그인 실패 -> 로그인 페이지로 이동
            return templates.TemplateResponse(
                request = request, 
                name = "login.html"
            )
    # return "Success"

@app.get('/register', response_class=HTMLResponse)
async def register_page_view(request: Request):
    return templates.TemplateResponse(
        request = request,
        name='register.html'
    )

@app.post('/register', response_class=HTMLResponse)
async def register(
    request: Request,
    username: str=Form(...), 
    email: str=Form(...),
    phone: str=Form(...),
    password:str=Form(...)
):
    # print(username, email, phone, password)
    
    users = db.users # table 지정
    user = users.find_one({'email' : email})
    if user == None:
        # 비밀번호 암호화
        hashed_pw = pbkdf2_sha256.hash(password+salt)

        result = users.insert_one({
        "username" : username,
        'email' : email,
        'phone' : phone,
        'password' : hashed_pw
    })
        print(result)
        return templates.TemplateResponse(
            request = request,
            name='login.html'
        )
        
    else:
        return templates.TemplateResponse(
            request = request,
            name='register.html'
        )