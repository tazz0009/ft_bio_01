from dataclasses import dataclass, asdict
from os import path, environ

base_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))


@dataclass
class Config:
    """
    기본  Configuration
    """
    BASE_DIR = base_dir

    DB_POOL_RECYCLE: int = 900
    DB_ECHO: bool = True


@dataclass
class LocalConfig(Config):
    PROJ_RELOAD: bool = True


@dataclass
class ProdConfig(Config):
    PROJ_RELOAD: bool = False


# def abc(DB_ECHO=None, DB_POOL_RECYCLE=None, **kwargs):
#     print(DB_ECHO, DB_POOL_RECYCLE)


# arg = asdict(LocalConfig())
# abc(**arg)


def conf():
    """
    환경 불러오기
    """
    config = dict(prod=ProdConfig, local=LocalConfig)
    # print(config)
    # print(environ.get("API_ENV", "local"))
    # print(config.get(environ.get("API_ENV", "local")))
    return config[environ.get("API_ENV", "local")]()
