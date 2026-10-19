from schema.response import TodoResponse  # 응답 모델 임포트
from fastapi import FastAPI, status

app = FastAPI()

# 할 일 저장
todos = [       # 임시 데이터 저장 -> 실제는 데이터 베이스에다가 관리
    {"id": 1, "title": "FastAPI 공부하기", "is_done": False},
    {"id": 2, "title": "운동하기", "is_done": True},
    {"id": 3, "title": "책 읽기", "is_done": False},
]

# 전체 할 일 조회
@app.get("/todos",
         response_model=list[TodoResponse],
         status_code=status.HTTP_200_OK)
def get_todos_handler():
    return todos