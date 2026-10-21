from pydantic import BaseModel

class BlogCreateRequest(BaseModel):
    title: str
    content: str

class BlogUpdateRequest(BaseModel):
    title: str | None = None
    content: str | None = None