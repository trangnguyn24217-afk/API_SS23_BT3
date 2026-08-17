from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from middleware.request_middleware import register_request_middleware
from routers.auth_router import router as auth_router
from routers.user_router import router as user_router
from routers.resource_router import router as resource_router

app = FastAPI(title="Secure Learning Resource API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PATCH", "DELETE", "OPTIONS"],
    allow_headers=["Authorization", "Content-Type"],
)

register_request_middleware(app)

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(resource_router)


@app.get("/health")
def health():
    return {"status": "UP"}
