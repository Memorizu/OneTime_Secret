import motor.motor_asyncio
from beanie import init_beanie

from source.settings import DB_PATH


def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(url=DB_PATH)
    await init_beanie(database=client['secrets'])
