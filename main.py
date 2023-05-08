import os

from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from fastapi import FastAPI

from routes import client

def custom_openapi():
    openapi_schema = get_openapi(
        title="Send mail",
        version="1.0.0",
        description="API to manage sending mails",
        routes=app.routes,
    )
    return openapi_schema

def create_app():
    app = FastAPI()

    if os.getenv('PYTHON_ENV') == 'dev':
        app.openapi = custom_openapi
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(client.router)

    return app

app = create_app()