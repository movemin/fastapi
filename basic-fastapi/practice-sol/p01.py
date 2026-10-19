from schema.response import TodoResponse # 응답 모델 임포트
from fastapi import FastAPI, status, HTTPException

app = FastAPI()

todos = [
    {"id": 1, "title": "FastAPI 공부하기", "is_done": False},
    {"id": 2, "title": "운동하기", "is_done": True},
    {"id": 3, "title": "책 읽기", "is_done": False},
]

# [문제 1] 단일 할 일 상세 조회
@app.get("/todos/{todo_id}",
         response_model=TodoResponse,
         status_code=status.HTTP_200_OK)

def get_todo_handler(todo_id: int):
    # 1. todos 목록에서 todo_id가 일치하는 항목 검색
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
        
    # 2. 일치하는 항목이 없을 경우 404 예외 발생
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Todo not found" 
    )