from fastapi import FastAPI
from starlette.applications import Starlette
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from starlette.responses import HTMLResponse


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
# @app.route('/index-gray.html')
# async def homepage(request):
#     return templates.TemplateResponse('index-gray.html', {'request': request}) 