from fastapi import Request, HTTPException
from app.config import redis_client

RATE_LIMIT = 5
WINDOW = 60


async def rate_limiter(request: Request):

    client_ip = request.client.host
    key = f"rate_limit:{client_ip}"

    current = redis_client.get(key)

    if current and int(current) >= RATE_LIMIT:
        raise HTTPException(
            status_code=429,
            detail="Too many requests. Please try again later."
        )

    pipe = redis_client.pipeline()
    pipe.incr(key, 1)
    pipe.expire(key, WINDOW)
    pipe.execute()