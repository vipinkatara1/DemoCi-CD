from fastapi import FastAPI, Request, Response, status
import schemas
from routes import zipapply
import time
from middlewares.middlewares import ResponseTimeMiddleware

app = FastAPI()

app.add_middleware(ResponseTimeMiddleware)

app.include_router(zipapply.router)
