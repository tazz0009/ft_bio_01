import datetime
from sqlalchemy import Column, Integer, String, DateTime, func
from .database import Base


class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    body = Column(String(500))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow,
                        onupdate=datetime.datetime.utcnow)

# for SQLITE
# class Blog(Base):
#     __tablename__ = 'blogs'

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String)
#     body = Column(String)
