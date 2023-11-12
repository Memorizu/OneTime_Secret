import os

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from dotenv import load_dotenv

from source.secret.tasks import fetch_expired_ttl

load_dotenv()

DB_PATH = os.getenv('DB_PATH')
DB_TEST_PATH = os.getenv('DB_TEST_PATH')
HEX_ENCODE_KEY = os.getenv('HEX_ENCODE_KEY')


scheduler = AsyncIOScheduler()
scheduler.add_job(fetch_expired_ttl, 'interval', hour=1)
