from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from .database import init_db
from .route import api


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield



def create_app():
    
    app = FastAPI(lifespan=lifespan)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "https://my-frontend.onrender.com",        
            "http://127.0.0.1:5500/frontend/template/contact.html",
            "http://localhost:5500/frontend/template/contact.html"
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api)

    
    return app
