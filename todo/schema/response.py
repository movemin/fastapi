from pydantic import BaseModel

# 할 일 응답 모델
class TodoResponse(BaseModel):  # 응답 모델 이름 정의

    # 할 일 데이터의 고유 아이디
    id: int

    # 할 일 데이터의 제목
    title: str

    # 할 일의 완료 여부
    is_done: bool