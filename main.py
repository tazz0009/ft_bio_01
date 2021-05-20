import uvicorn
from fastapi import FastAPI
from app.common.config import conf
from app.database import models
from app.database.database import engine
from app.routes import index, blog


def create_app():
    """
    앱 함수 실행
    """
    # c = conf()
    app = FastAPI()

    # 데이터 베이스 이니셜라이즈
    models.Base.metadata.create_all(engine)

    # 레디스 이니셜라이즈
    # 미들웨어 정의
    # 라우터 정의
    app.include_router(index.router)
    app.include_router(blog.router)
    return app


app = create_app()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0",
                port=8000, reload=conf().PROJ_RELOAD)
