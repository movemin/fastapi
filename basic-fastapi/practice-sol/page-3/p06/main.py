from schema.request import BookCreateRequest, BookUpdateRequest
from schema.response import BookResponse
from fastapi import FastAPI, status, HTTPException

app = FastAPI()

books = [
    {"id": 1, "title": "FastAPI 완전 가이드", "author": "김파이썬", "is_available": True},
    {"id": 2, "title": "클린 코드", "author": "로버트 C. 마틴", "is_available": False}
]

# 전체 도서 조회
@app.get(
    "/books",
    response_model=list[BookResponse],
    status_code=status.HTTP_200_OK
)
def get_books_handler():
    return books

# 단일 도서 조회
@app.get(
    "/books/{book_id}",
    response_model=BookResponse,
    status_code=status.HTTP_200_OK
)
def get_book_handler(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found"
    )

# 도서 등록
@app.post(
    "/books",
    response_model=BookResponse,
    status_code=status.HTTP_201_CREATED
)
def create_book_handler(body: BookCreateRequest):
    new_id = max([book["id"] for book in books], default=0) + 1
    new_book = {
        "id": new_id,
        "title": body.title,
        "author": body.author,
        "is_available": body.is_available
    }
    books.append(new_book)
    return new_book

# 도서 정보 수정 (부분 수정 PATCH)
@app.patch(
    "/books/{book_id}",
    response_model=BookResponse,
    status_code=status.HTTP_200_OK
)
def update_book_handler(book_id: int, body: BookUpdateRequest):
    for book in books:
        if book["id"] == book_id:
            if body.title is not None:
                book["title"] = body.title
            if body.author is not None:
                book["author"] = body.author
            if body.is_available is not None:
                book["is_available"] = body.is_available
            return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found"
    )

# 도서 삭제
@app.delete(
    "/books/{book_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_book_handler(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found"
    )