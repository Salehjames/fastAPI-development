from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

@app.get("/api/sum")
def get_sum(num1: int = Query(...), num2: int = Query(...)):
    """
    Calculate the sum of two numbers.

    Args:
        num1 (int): The first number as a query parameter.
        num2 (int): The second number as a query parameter.

    Returns:
        dict: A dictionary with the sum of num1 and num2.
    """
    return {"sum": num1 + num2}

class Numbers(BaseModel):
    num1: int
    num2: int

@app.post("/api/difference")
def post_difference(numbers: Numbers):
    """
    Calculate the difference between two numbers.

    Args:
        numbers (Numbers): A Pydantic model with num1 and num2 as integers.

    Returns:
        dict: A dictionary with the difference between num1 and num2.
    """
    return {"difference": numbers.num1 - numbers.num2}
