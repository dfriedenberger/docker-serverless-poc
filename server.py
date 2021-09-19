from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from src.docker_util import call_serverless

app = FastAPI()

app.add_middleware(GZipMiddleware, minimum_size=500)


@app.get("/", response_class=HTMLResponse)
async def read_root():
    command = "echo {}".format("Hello World!")
    result = call_serverless("hello_world",command)
    return """
        <html>
            <head>
                <title>Call Serverless hello_world</title>
            </head>
            <body>
                <p>{0}<p>
            </body>
        </html>
    """.format("<br>".join(result))

app.mount("/assets", StaticFiles(directory="assets"), name="assets")
