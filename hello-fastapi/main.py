from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

# 서버 실행
@app.get("/") # 엔드포인트
def root_handler():
    return {"message": "Hello World"}

# 경로 사용
@app.get("/login")      # GET 요청과 경로 매핑 설정, 엔드포인트
def login_handler():    # 요청을 처리하는 함수 정의
    return {"message": "Hello, FastAPI"}

# 경로 변수 사용
@app.get("/users/{user_id}") # 엔드포인트
def user_handler(user_id: int):
    return {"user_id": user_id, "message": f"사용자 {user_id} 정보 조회"}

# 쿼리 파라미터 사용
@app.get("/items")
def read_items_handler(max_price: int | None = None):
    return {"max_price": max_price}

# 아이템 모델 정의
class Item(BaseModel): # 요청 본문 검증을 위한 Item 모델 정의
    name: str
    price: int
    in_stock: bool = True

# 새 아이템 등록
@app.post("/items", response_model=Item) # 응답 데이터를 Item 모델로 지정
def create_item_handler(item: Item):
    return item # Item 객체를 그대로 반환

# 경로 변수, 쿼리 파라미터, 요청 본문 혼합 사용
@app.put("/items/{item_id}")
def update_item_handler(item_id: int, assignee: str, item: Item):
    return {
        "item_id": item_id,
        "assignee": assignee, # 담당자 또는 작업자
        "item": item
    }