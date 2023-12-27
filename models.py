"""
게시판의 질문과 답변 데이터를 저장하기 위한 모델
"""
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


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

