import datetime

from pydantic import BaseModel  # pydantic : FastAPI의 입출력 스펙을 정의하고 값을 검증하는데 활용


class Question(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime.datetime
