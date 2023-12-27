from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import contextlib

SQLALCHEMY_DATABASE_URL = "sqlite:///./api.db"  # Project Root에 file로 저장

engine = create_engine(
    url=SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# DB 접속을 위한 세션 생성
SessionLocal = sessionmaker(
    autocommit=False, # commit 사인이 없는 경우 DB를 갱신하지 않음.
    autoflush=False,
    bind=engine
)

Base = declarative_base()


# Dependency Injection(의존성 주입)
# DB 세션 생성 및 종료
@contextlib.contextmanager
def get_db():
    db = SessionLocal()
    
    try:
        yield db
    
    finally:
        db.close()