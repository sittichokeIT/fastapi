from fastapi import FastAPI
from routes.route_user import user
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


origins = [
    "http://127.0.0.1:8000",
    "http://127.0.0.1"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user)
