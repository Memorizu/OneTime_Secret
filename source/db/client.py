import motor.motor_asyncio
from beanie import init_beanie

from source.secret.model import Secret
from source.settings import DB_PATH


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(host=DB_PATH)
    await init_beanie(database=client['secrets'], document_models=[Secret])
