from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

@app.get("/api/sum")
def get_sum(num1: int = Query(...), num2: int = Query(...)):
    return {"sum": num1 + num2}
