from fastapi import FastAPI

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