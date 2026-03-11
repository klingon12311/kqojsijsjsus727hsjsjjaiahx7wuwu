import os

from dotenv import load_dotenv

load_dotenv(".env")

API_ID: int = os.getenv('API_ID', 24980886)
API_HASH: str = os.getenv('API_HASH', "51a392c893abd52f04186bb44ba3b3aa")

BOT_TOKEN = os.getenv("BOT_TOKEN")

OWNER_ID = int(os.getenv("OWNER_ID"))

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT"))

MAX_BOT = int(os.getenv("MAX_BOT"))

RMBG_API = os.getenv("RMBG_API")

OPENAI_KEY = os.getenv("OPENAI_KEY")

MONGO_URL = os.getenv("MONGO_URL")
