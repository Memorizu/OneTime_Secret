import motor.motor_asyncio
import pytest
from beanie import init_beanie
from httpx import AsyncClient

from source.main import app
from source.secret.model import Secret
from source.settings import DB_TEST_PATH


@pytest.fixture
def wrong_get_one_secret():
    return {
        'message': 'test_secret'
    }


@pytest.fixture
def secret_key():
    return 'test_secret'


@pytest.fixture
def get_one_secret():
    return {
        'message': 'test_secret',
        'secret_key': 'test_secret'
    }


@pytest.fixture
def wrong_secret_key():
    return 'wrong'


@pytest.fixture(scope='function')
async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(host=DB_TEST_PATH)
    db = client['secrets']
    await init_beanie(database=db, document_models=[Secret])
    yield db
    await db.drop_collection('Secret')


@pytest.fixture(scope='function')
async def client():
    async with AsyncClient(app=app, base_url='http://test') as ac:
        yield ac
