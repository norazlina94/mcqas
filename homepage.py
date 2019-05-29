from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from starlette.applications import Starlette
from starlette.templating import Jinja2Templates
from starlette.responses import Response
from starlette.responses import HTMLResponse
from starlette.testclient import TestClient

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

@app.route('/')
async def homepage(request):
    return templates.TemplateResponse('item.html', {'request': request})

app.mount("/static", StaticFiles(directory="static"), static)

@app.route('/')
async def homepage(request):
    template = "item.html"
    context = {"request": request}
    return templates.TemplateResponse(template, context)

    # if __name__ == "__main__":
    # uvicorn.run(app, host='127.0.0.1', port=8000)

class app:
    def __init__(self, scope):
        assert scope['type'] == 'http'
        self.scope = scope

    async def __call__(self, receive, send):
        response = HTMLResponse('<html><body>Hello, world!</body></html>')
        await response(receive, send)
# @app.route('/')
# async def homepage(request):
#     templates = "item.html"
#     context = {"request": request}
#     return templates.TemplateResponse(templates, context)

# def test_homepage():
#     client = TestClient(app)
#     response = client.get('/')
#     assert response.status_code == 200
#     assert response.templates.name == 'item.html'
#     assert "request" in response.context

