import httpx
from app.config import BASE_URL


async def send_user(user: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(BASE_URL, json=user)

        response.raise_for_status()
        return response.json()