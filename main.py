import os

import httpx
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ton domaine portfolio
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")

print("TELEGRAM_TOKEN:", TELEGRAM_TOKEN)
print("TELEGRAM_CHAT_ID:", TELEGRAM_CHAT_ID)


class ContactMessage(BaseModel):
    name: str
    email: str
    message: str


@app.post("/contact")
async def contact(data: ContactMessage):
    text = (
        f"📬 *Nouveau message portfolio*\n\n"
        f"👤 *Nom :* {data.name}\n"
        f"📧 *Email :* {data.email}\n"
        f"💬 *Message :*\n{data.message}"
    )
    async with httpx.AsyncClient() as client:
        r = await client.post(
            f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
            json={
                "chat_id": TELEGRAM_CHAT_ID,
                "text": text,
                "parse_mode": "Markdown",
            },
        )
        print("Telegram response:", r.status_code, r.text)  # 👈 ajoute ça
    return {"ok": True}
