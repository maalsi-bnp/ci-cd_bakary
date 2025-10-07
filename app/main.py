from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="TP4 CI/CD Demo")

class SumRequest(BaseModel):
    a: float
    b: float

@app.get("/")
def read_root():
    return {"message": "Hello — CI/CD TP4 ready!"}

@app.post("/sum")
def compute_sum(req: SumRequest):
    """Simple function that we will test"""
    return {"result": req.a + req.b}

# also expose utility function for unit tests
def add(a: float, b: float) -> float:
    return a + b
