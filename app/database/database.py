from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# for SQLITE
# SQLALCHAMY_DATABASE_URL = 'sqlite:///./blog.db'
#
# engine = create_engine(SQLALCHAMY_DATABASE_URL, connect_args={
#                        "check_same_thread": False})

SQLALCHAMY_DATABASE_URL = 'mysql://springtest:1234qwer@192.168.0.30:3306/testdb?charset=utf8mb4'

engine = create_engine(SQLALCHAMY_DATABASE_URL, echo=True,
                       pool_recycle=900, pool_pre_ping=True)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False,)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
