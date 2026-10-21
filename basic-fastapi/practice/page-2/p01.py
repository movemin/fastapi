"""
[문제 1] 단일 할 일 상세 조회 (GET /todos/{todo_id})

문제 설명
todos 목록에서 특정 id를 가진 할 일 항목 하나를 조회하는 API 엔드포인트를 작성하세요.

요구사항:
  1. Path Parameter로 `todo_id` (`int`)를 전달받습니다.
  2. `todo_id`에 해당하는 항목이 존재할 경우, Status Code **200 OK**와 함께 해당 객체를 반환합니다.
  3. 해당하는 `todo_id`가 존재하지 않을 경우, FastAPI의 `HTTPException`을 활용하여 Status Code **404 Not Found** 및 메시지 `{"detail": "Todo not found"}`를 반환해야 합니다.

입출력 예시
요청: GET /todos/1
응답 (200 OK): {"id": 1, "title": "FastAPI 공부하기", "is_done": false}

요청: GET /todos/99
응답 (404 Not Found):
{"detail": "Todo not found"}
"""