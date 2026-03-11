import aiohttp
import filetype
from io import BytesIO
from PyroUbot import *
from httpx import AsyncClient, Timeout

fetch = AsyncClient(
    http2=True,
    verify=False,
    headers={
        "Accept-Language": "en-US,en;q=0.9,id-ID;q=0.8,id;q=0.7",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edge/107.0.1418.42",
    },
    timeout=Timeout(20),
)

async def upload_media(m):
    media = await m.reply_to_message.download()
    url = "https://itzpire.com/tools/upload"
    with open(media, "rb") as file:
        files = {"file": file}
        response = await fetch.post(url, files=files)
    if response.status_code == 200:
        data = response.json()
        link = data["fileInfo"]["url"]
        return link
    else:
        return f"{response.text}"
