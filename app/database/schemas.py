from pydantic import BaseModel
from datetime import datetime


class BlogBase(BaseModel):
    id: int
    title: str
    body: str

    class Config():
        orm_mode = True


class ShowBlog(BaseModel):
    title: str
    body: str

    class Config():
        orm_mode = True
