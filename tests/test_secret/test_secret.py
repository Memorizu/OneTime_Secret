
from httpx import AsyncClient


async def test_get_all_secrets(init_db, client: AsyncClient):
    response = await client.get('/test_secret/')
    assert len(response.json()) == 0
    assert response.status_code == 200


async def test_create_secret(init_db, client: AsyncClient, get_one_secret):
    response = await client.post('/test_secret/', json=get_one_secret)
    assert response.status_code == 201
    assert response.json() == {'message': 'Secret created successfully'}


async def test_create_secret_negative(init_db, client: AsyncClient, wrong_get_one_secret):
    response = await client.post('/test_secret/', json=wrong_get_one_secret)
    assert response.status_code == 422


async def test_get_secret(init_db, client: AsyncClient, get_one_secret, secret_key):
    await client.post('/test_secret/', json=get_one_secret)
    response = await client.get(f'/test_secret/{secret_key}')
    assert response.status_code == 200
    assert response.json() == 'test_secret'


async def test_get_secret_negative(init_db, client: AsyncClient, get_one_secret, wrong_secret_key):
    await client.post('/test_secret/', json=get_one_secret)
    response = await client.get(f'/test_secret/{wrong_secret_key}')
    assert response.status_code == 200
    assert response.json() is None
