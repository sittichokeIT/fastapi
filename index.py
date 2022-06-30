from imp import reload
from re import I
from fastapi import FastAPI
from routes.route_user import user
from routes.route_province import province
from starlette.middleware.cors import CORSMiddleware
import uvicorn
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
app.include_router(province)

# if __name__ == "__main__":
#     uvicorn.run("index:app", host="127.0.0.2", port=8000, log_level="info",reload =True)
