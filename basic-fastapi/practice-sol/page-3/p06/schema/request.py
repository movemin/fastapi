from pydantic import BaseModel
from typing import Optional

class BookCreateRequest(BaseModel):
    title: str
    author: str
    is_available: bool = True

class BookUpdateRequest(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    is_available: Optional[bool] = None