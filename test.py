import os


from typing import List

from fastapi import FastAPI, File, Form, UploadFile

from starlette.requests import Request
from starlette.applications import Starlette
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from starlette.responses import HTMLResponse


import myhandler as my

templates = Jinja2Templates(directory='templates')


static = FastAPI(openapi_prefix="/static")
# css = FastAPI(openapi_prefix="/css")
# js = FastAPI(openapi_prefix="/js")
images = FastAPI(openapi_prefix="/images")

app = Starlette(debug=True)
app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')
# app.mount('/css', StaticFiles(directory='css'), name='css')
# app.mount('/js', StaticFiles(directory='js'), name='js')
app.mount('/images', StaticFiles(directory='images'), name='images')

@app.route('/')
async def homepage(request):
    return templates.TemplateResponse('index.html', {'request': request})
     
@app.route('/index.html')
async def homepage(request):
    return templates.TemplateResponse('index.html', {'request': request})

@app.route('/contact.html')
async def homepage(request):
    return templates.TemplateResponse('contact.html', {'request': request})

@app.route('/client.html')
async def homepage(request):
    return templates.TemplateResponse('client.html', {'request': request})

@app.route('/services.html')
async def homepage(request):
    return templates.TemplateResponse('services.html', {'request': request})

@app.route('/quotes.html')
async def homepage(request):
    return templates.TemplateResponse('quotes.html', {'request': request})

@app.route('/login.html')
async def homepage(request):
    return templates.TemplateResponse('login.html', {'request': request})

@app.route('/member.html')
async def homepage(request):
    return templates.TemplateResponse('member.html', {'request': request})    

@app.route('/eBloodFilm.html')
async def homepage(request):
    return templates.TemplateResponse('eBloodFilm.html', {'request': request})     

@app.post('/orderdesk')
async def homepage(request: Request, 
                price: float = Form(...), lot: int = Form(...),
                itemname: str = Form(...), action: str = Form(...), connect: int = Form(...)):
    print('--------------- quotes received {} {}'.format(price, lot))
    print('--------------- quotes received {} {} connect {}'.format(itemname, action, connect))
    my.enter_tst('Transactions', 'lina', itemname, action, lot, price)
    found = my.retrieve_tst('Transactions', 'lina', 'SELL')
    print('............... quotes found {}'.format(found))
    return templates.TemplateResponse('quotes.html', {'request': request})

@app.post('/ebloodfilmcount')
async def homepage(request: Request, 
                count1: int = Form(...), count2: int = Form(...), count3: int = Form(...),
                count4: int = Form(...), count5: int = Form(...), count6: int = Form(...),
                count7: int = Form(...), count8: int = Form(...), count9: int = Form(...),
                count10: int = Form(...), count11: int = Form(...), count12: int = Form(...),
                unit1: int = Form(...),
                unit2: int = Form(...), unit3: int = Form(...), unit4: int = Form(...),
                unit5: int = Form(...), unit6: int = Form(...), unit7: int = Form(...),
                unit8: int = Form(...), unit9: int = Form(...), unit10: int = Form(...),
                unit11: int = Form(...), unit12: int = Form(...),
                action: str = Form(...), connect: int = Form(...)):
    # print('---------------  received {} {}'.format(price, lot))
    # print('---------------  received {} {} connect {}'.format(action, connect))
    my.enter_tst1('ebloodfilm', 'lina', count1,count2,count3,count4,count5,count6,count7,count8,count9,count10,count11,count12,
        unit1,unit2,unit3,unit4,unit5,unit6,unit7,unit8,unit9,unit10,unit11,unit12)
    found = my.retrieve_tst1('ebloodfilm', 'lina')
    print('...............  found {}'.format(found))
    return templates.TemplateResponse('eBloodFilm.html', {'request': request})    

@app.post("/upload1")
async def create_file(files: List[UploadFile] = File(...)):
    info = []
    for f in files:
        bt = f.file.read()
        nf = open('files/{}'.format(f.filename), 'wb')
        nf.write(bt)
        nf.close()
        info += [ (f.filename, f.content_type, len(bt)) ]
    return {"filenames": info}

