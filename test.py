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

