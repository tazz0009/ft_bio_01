from typing import List, Optional
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..database import schemas, database
from ..repository import blog

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)

get_db = database.get_db


@router.get('/', response_model=List[schemas.BlogBase])
def all(db: Session = Depends(get_db)):
    """
    모든 Blog 가져오기 API
    """
    return blog.get_all(db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id: int, db: Session = Depends(get_db)):
    """
    단일 Blog 가져오기 API
    """
    return blog.show(id, db)


@router.post('/', status_code=status.HTTP_201_CREATED,)
def create(request: schemas.ShowBlog, db: Session = Depends(get_db)):
    """
    Blog 생성 API
    """
    return blog.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_202_ACCEPTED)
def destroy(id: int, db: Session = Depends(get_db)):
    """
    Blog 삭제 API
    """
    return blog.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.ShowBlog, db: Session = Depends(get_db)):
    """
    Blog 수정 API
    """
    return blog.update(id, request, db)
