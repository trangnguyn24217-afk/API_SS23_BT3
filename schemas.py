from pydantic import BaseModel, Field, HttpUrl


class LoginRequest(BaseModel):
    username: str = Field(min_length=1)
    password: str = Field(min_length=1)


class ResourceCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: str = Field(min_length=1)
    url: HttpUrl


class PublishRequest(BaseModel):
    is_published: bool


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
