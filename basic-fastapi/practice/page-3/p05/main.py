"""
[문제 5] 회원(User) 관리 REST API 구현

**문제 설명**
회원 관리 프로젝트를 새로 생성한 뒤 다음 조건을 만족하는 REST API를 구현하세요.

**요구사항**
  1. 전체 회원 조회(GET /users), 단일 회원 조회(GET /users/{user_id}), 회원가입(POST /users), 회원정보 수정(PUT /users/{user_id}), 회원 탈퇴(DELETE /users/{user_id}) 기능을 모두 구현하세요.
  2. 회원 데이터는 id(정수형), username(문자열), email(문자열)의 세 필드로 구성됩니다.
  3. 요청 모델과 응답 모델은 각각 schema 패키지의 request.py(UserCreateRequest, UserUpdateRequest)와 response.py(UserResponse)에 정의하고, API 구현은 main.py에 작성합니다.
  4. 존재하지 않는 user_id 접근 시 Status Code 404 Not Found와 함께 {"detail": "User not found"}를 반환해야 합니다.
"""

from schema.request import UserCreateRequest, UserUpdateRequest
from schema.response import UserResponse
from fastapi import FastAPI, status, HTTPException

app = FastAPI()

# 회원 저장소 (인메모리 데이터)
users = [
    {"id": 1, "username": "alex", "email": "alex@example.com"},
    {"id": 2, "username": "maria", "email": "maria@example.com"}
]

# TODO 1: 전체 회원 조회 (GET /users)

# TODO 2: 단일 회원 조회 (GET /users/{user_id})

# TODO 3: 회원 가입 (POST /users) # TODO 4: 회원 정보 수정 (PUT /users/{user_id})

# TODO 5: 회원 탈퇴 (DELETE /users/{user_id})
