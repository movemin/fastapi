from pydantic import BaseModel

# 할 일 생성 요청 모델
class TodoCreateRequest(BaseModel):  # 생성 요청 모델 이름 정의
    title: str                       # 요청 본문 필드 구성
    is_done: bool = False

# 할 일 수정 요청 모델
class TodoUpdateRequest(BaseModel):
    title: str | None = None
    is_done: bool | None = None