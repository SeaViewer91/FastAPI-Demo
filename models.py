"""
게시판의 질문과 답변 데이터를 저장하기 위한 모델
"""
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


"""
pip install alembic

모델 정의 후 'alembic revision --autogenerate' 명령어로 리비전 파일 생성
이후 'alembic upgrade head' 명령어로 리비전 파일 실행

main.py에 models.Base.metadata.create_all(bind=engine) 코드 추가 시
alembic 없이 테이블 생성이 가능하나, 이경우 한번 생성된 테이블에 대한 변경관리가 불가
"""

class Question(Base):
    __tablename__ = "question"
    
    id = Column(Integer, primary_key=True)  # 질문 데이터의 고유번호
    subject = Column(String, nullable=False)  # 질문 게시물의 제목
    content = Column(Text, nullable=False)  # 질문 내용
    create_date = Column(DateTime, nullable=False)  # 질문 작성일시
    

class Answer(Base):
    __tablename__ = "answer"
    
    id = Column(Integer, primary_key=True)  # 답변 데이터의 고유번호
    content = Column(Text, nullable=False)  # 답변 내용
    create_date = Column(DateTime, nullable=False)  # 답변 작성일시  
    question_id = Column(Integer, ForeignKey("question.id"))  # 질문 데이터의 고유번호(외래키)
    question = relationship("Question", backref="answers")  # 하나의 질문에 여러 답변이 생성되는 것을 고려하여 역참조 설정

