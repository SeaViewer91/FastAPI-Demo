# FastAPI-Demo


# Project Architecture
```
├─main.py
├─database.py
├─models.py
├─domain
│  └─answer
│  └─question
│  └─user
└─frontend

```
* main.py : API 관련 코드
* database.py : DB관련 코드 및 configuration
* modles.py : 모델 클래스
* domain : Project 도메인을 위한 데이터 및 관련 코드
* frontend : Svelte 프레임워크의 소스 및 빌드 파일