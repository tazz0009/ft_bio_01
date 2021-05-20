# FastAPI Tutorials

Python FastAPI 사용해서 API 서버 간단 구축

## Install and Setup

- 가상환경설치

```
python3 -m venv fastapi-env
fastapi-env\Scripts\activate.bat
```

- 아나콘다 가상환경설치

```
conda create -n fastapi-env
conda info --envs
conda activate fastapi-env
conda deactivate
```

- fastAPI, uvicorn 설치

```
pip3 install fastapi
python -m pip install --upgrade pip
pip install uvicorn
uvicorn --version
```

- requirements.txt 파일 생성

```
pip3 install -r requirements.txt
```

- main.py 파일 생성
- 서버 start

```
python main.py
```

## Git setting

- git 초기화

```
git init
```

- .gitignore 파일 생성
- git commit

```
git add .
git commit -m "let learn fastAPI"
```

## API Docs

- http://127.0.0.1:8000/docs
