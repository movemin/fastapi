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