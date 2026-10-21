"""
[문제 3] 할 일 완료 상태 토글 (PATCH /todos/{todo_id}/done)
    문제 설명: 특정 할 일의 완료 여부(is_done) 상태를 반전(True <-> False)시키는 엔드포인트를 작성하세요.
    
    요구사항:
        Path Parameter로 todo_id (int)를 전달받습니다.
        해당 id가 존재하면 is_done 값을 반대로 변경하고, Status Code 200 OK와 함께 수정된 Todo 객체를 반환합니다.
        해당 id가 존재하지 않으면 Status Code 404 Not Found를 반환합니다.
        
    입출력 예시:
        요청: 
            PATCH /todos/1/done (기존 is_done이 false인 경우)
        응답 (200 OK):
            {"id": 1, "title": "FastAPI 공부하기", "is_done": true}
"""