from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

@app.get("/api/sum")
def get_sum(num1: int = Query(...), num2: int = Query(...)):
    return {"sum": num1 + num2}

class Numbers(BaseModel):
    num1: int
    num2: int

@app.post("/api/difference")
def post_difference(numbers: Numbers):
    return {"difference": numbers.num1 - numbers.num2}