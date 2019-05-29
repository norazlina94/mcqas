from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from starlette.applications import Starlette
from starlette.templating import Jinja2Templates


templates = Jinja2Templates(directory='templates')

app = Starlette(debug=True)
app = FastAPI()


@app.get("/app")
def read_main():
    return {"message": "Hello World from main app"}


static = FastAPI(openapi_prefix="/static")


@static.get("/sub")
def read_sub():
    return {"message": "Hello World from sub API"}

@app.get('/')
async def homepage(request):
    return templates.TemplateResponse('item.html', {'request': request})

app.mount("/static", StaticFiles(directory="static"), static)
templates = Jinja2Templates(directory="templates")

@app.get("/Request/{Request}")
async def read_item(Request):
    return {"Request": Request}



@app.get("/items/{id}")

async def read_item(request: str, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})

@app.route('/')
async def homepage(request):
    return templates.TemplateResponse('item.html', {'request': request})
    
    # def test_homepage():
    # client = TestClient(app)
    # response = client.get("/")
    # assert response.status_code == 200
    # assert response.template.name == 'item.html'
    # assert "request" in response.context