"""
[문제4] blog 프로젝트를 새로 생성한 뒤 다음 조건을 만족하는 REST API를 구현하세요.
(1) 전체 게시글 조회, 단일 게시글 조회, 게시글 생성, 게시글 수정, 게시글 삭제 기능을 모두 구현하세요.
(2) 게시글은 id(정수형), title(문자열), content(문자열)의 세 필드로 구성됩니다.
(3) 요청 모델과 응답 모델은 각각 [schema] 패키지의 request.py와 response.py에 정의하고, API 구현은 main.py에 작성합니다.
"""
from schema.request import BlogCreateRequest, BlogUpdateRequest
from schema.response import BlogResponse
from fastapi import FastAPI, status, HTTPException

app = FastAPI()

# 게시글 저장
blogs = [
    {}
]

# 전체 게시글 조회
@app.get(
        "/blogs",
        response_model=list[BlogResponse],
        status_code=status.HTTP_200_ok
)
def get_blog_handler():
    return blogs

# 단일 게시글 조회
@app.get(
        "/blogs/{user_id}",
        response_model=BlogResponse,
        status_code=status.HTTP_200_ok
)
def get_blog_handler(user_id: int):
    for blog in blogs:
        if blog["id"] == user_id:
            return blog
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")

# 게시글 생성
@app.post(
        "/blogs",
        response_model=BlogResponse,
        status_code=status.HTTP_201_CREATED
)
def create_blog_handler(body: BlogCreateRequest):
    new_blog = {
        "id": len(blogs) + 1,
        "title": body.title,
        "content": body.content
    }
    blogs.append(new_blog)
    return new_blog

# 게시글 수정
@app.patch(
        "/blogs/{user_id}",
        response_model=BlogResponse,
        status_code=status.HTTP_200_ok
)
def update_blog_handler(user_id: int, body: BlogUpdateRequest):
    for blog in blogs:
        if blog["id"] == user_id:
            if blog["title"] is not None:
                blog["title"] = body.title
            if blog["content"] is not None:
                blog["content"] = body.content
            return blog
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")

@app.delete(
        "/blogs/{user_id}",
        status_code=status.HTTP_204_NO_CONTENT
)
def delete_blog_handler(user_id: int):
    for blog in blogs:
        if blog["id"] == user_id:
            blogs.remove(blog)
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")