import motor.motor_asyncio
from beanie import init_beanie

from loger.loger import get_loger
from source.secret.model import Secret
from source.settings import DB_PATH


loger = get_loger('motor_client')


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(host=DB_PATH)
    db = client['secrets']
    loger.info('connecting to database')
    await init_beanie(database=db, document_models=[Secret])
    await client.server_info()
    loger.info('connected to database')
    return db
