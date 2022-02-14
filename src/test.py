from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/test')
def index():
    return {"data": "Hello!"}