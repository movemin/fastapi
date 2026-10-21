from schema.response import TodoResponse  # 응답 모델 임포트
from schema.request import TodoCreateRequest, TodoUpdateRequest  # 생성 요청 모델 임포트
from fastapi import FastAPI, status, HTTPException

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

# 단일 할 일 조회
@app.get(       # 경로 변수를 사용하는 GET API 정의
    "/todos/{todo_id}",
    response_model=TodoResponse,
    status_code=status.HTTP_200_OK
)
def get_todo_handler(todo_id: int):
    for todo in todos:  # 단일 데이터 탐색
        if todo["id"] == todo_id:
            return todo
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")

@app.post(       # 경로 변수를 사용하는 GET API 정의
    "/todos",
    response_model=TodoResponse,
    status_code=status.HTTP_201_CREATED
)
def create_todos_handler(body: TodoCreateRequest):     # 요청 본문을 매개변수로 받기
    new_todo = {                    # 새 할 일 데이터 생성
        "id": len(todos) + 1,       # id 값 생성
        "title": body.title,
        "is_done": body.is_done
    }
    todos.append(new_todo)          # 리스트에 새 할 일 추가 후 응답 반환
    return new_todo

# 할 일 수정
@app.patch( "/todos/{todo_id}",
            response_model=TodoResponse,
            status_code=status.HTTP_200_OK
)
def update_todos_handler(todo_id: int, body: TodoUpdateRequest):
    for todo in todos:                              # 수정 대상 데이터 탐색
        if todo["id"] == todo_id:
            if body.title is not None:              # title 필드 조건부 수정
                todo["title"] = body.title
            if body.is_done is not None:            # is_done 필드 조건부 수정
                todo["is_done"] = body.is_done
            return todo                             # 수정된 데이터 반환
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")  # 예외 처리

@app.delete("/todos/{todo_id}",
            status_code=status.HTTP_204_NO_CONTENT
)
def delete_todos_handler(todo_id: int):
    for todo in todos:              # 삭제 대상 데이터 탐색
        if todo["id"] == todo_id:
            todos.remove(todo)      # 데이터 삭제
            return                  # 응답 본문 없이 함수 종료
    raise HTTPException(status_code=status.HTTP_404_BAD_REQUEST, detail="Todo not found")