# main.py
from fastapi import FastAPI

app = FastAPI()

# 直接在 main.py 中定义路由
@app.get("/items")
def get_items():
    return {"message": "This is the /items endpoint!"}

@app.get("/")
def read_root():
    return {"message": "Welcome to the File Parser API!"}
