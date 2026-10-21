"""
[문제 6] 도서(Book) 대여 관리 REST API 구현

**문제 설명**
도서관 시스템 구축을 위해 다음 조건을 만족하는 도서(Book) 관리 REST API를 구현하세요.

**요구사항**
  1. 전체 도서 조회(GET /books), 단일 도서 조회(GET /books/{book_id}), 도서 등록(POST /books), 도서 정보 수정(PATCH /books/{book_id}), 도서 삭제(DELETE /books/{book_id}) 기능을 모두 구현하세요.
  2. 도서 데이터는 id(정수형), title(문자열), author(문자열), is_available(불리언)의 네 필드로 구성됩니다.
  3. 요청 모델과 응답 모델은 각각 schema 패키지의 request.py(BookCreateRequest, BookUpdateRequest)와 response.py(BookResponse)에 정의하고, API 구현은 main.py에 작성합니다.
  4. 존재하지 않는 book_id 접근 시 Status Code 404 Not Found와 함께 {"detail": "Book not found"}를 반환해야 합니다.
"""
from schema.request import BookCreateRequest, BookUpdateRequest
from schema.response import BookResponse
from fastapi import FastAPI, status, HTTPException

app = FastAPI()

# 도서 저장소 (인메모리 데이터)
books = [
    {"id": 1, "title": "FastAPI 완전 가이드", "author": "김파이썬", "is_available": True},
    {"id": 2, "title": "클린 코드", "author": "로버트 C. 마틴", "is_available": False}
]

# TODO 1: 전체 도서 조회 (GET /books)

# TODO 2: 단일 도서 조회 (GET /books/{book_id})

# TODO 3: 도서 등록 (POST /books)

# TODO 4: 도서 정보 수정 (PATCH /books/{book_id})

# TODO 5: 도서 삭제 (DELETE /books/{book_id})
