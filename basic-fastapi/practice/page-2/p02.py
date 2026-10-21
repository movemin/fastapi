"""
[문제 2] 새로운 할 일 생성 (POST /todos)

문제 설명: 새로운 할 일을 목록에 추가하는 엔드포인트를 작성하세요.

요구사항:
  1. Request Body로 할 일의 제목(title: str)을 전달받습니다. (Pydantic Request 스키마 작성 필요)
  2. 새로 생성되는 Todo의 id는 기존 todos 항목 중 최대 id + 1로 자동 생성하며, is_done 기본값은 False로 설정합니다.
  3. 성공적으로 추가되면 Status Code 201 Created와 함께 생성된 Todo 객체를 반환합니다.

입출력 예시:

요청: POST /todos

{"title": "파이썬 프로젝트 만들기"}

응답 (201 Created):


{"id": 4, "title": "파이썬 프로젝트 만들기", "is_done": false}

"""