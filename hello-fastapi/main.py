from fastapi import FastAPI

app = FastAPI()

# 서버 실행
@app.get("/")
def root_handler():
    return {"message": "Hello World"}

@app.get("/login")
def login_handler():
    return {"message": "Hello, FastAPI"}