from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from domain.question import question_schema
from models import Question
from typing import List  # Python 3.10 미만에서 적용

router = APIRouter(
    prefix="/api/question"
)

# @rounter.get("/list", response_model=list[question_schema.Question])  # 파이썬 3.10을 위한 코드
@router.get("/list", response_model=List[question_schema.Question])  # 스키마를 적용하여 입출력 스펙을 컨트롤
def question_list(db: Session = Depends(get_db)):
    _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    
    return _question_list    