import os

SECRET_KEY = os.getenv("SECRET_KEY", "training-secret-key")
ALGORITHM = "HS256"
ACCESS_TOKEN_MINUTES = 30

ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:5173",
]
