from fastapi import FastAPI, Depends
from app.limiter import rate_limiter

app = FastAPI()


@app.get("/")
def home():
    return {"message": "API Rate Limiter Running"}


@app.get("/data", dependencies=[Depends(rate_limiter)])
def get_data():
    return {"message": "You accessed a rate limited endpoint"}