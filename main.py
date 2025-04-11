# main.py
from fastapi import FastAPI
from file_parser.router import router  # 你自己写的 router

app = FastAPI()

app.include_router(router)
