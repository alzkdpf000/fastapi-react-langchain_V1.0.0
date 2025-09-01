from fastapi import FastAPI
from typing import Optional
from model_loader import ModelLoader
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()


origins = [
    "http://localhost:5173"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)


loader = ModelLoader()
loader.load()

@app.get("/")
async def root():
    return {"message" : "Hello world"}

@app.get("/home")
async def home(query: Optional[str] = None):
    if query:
        return { "response" : loader.run(query)["result"]}
    return { "response" : "질문이 없어"}
