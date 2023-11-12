from typing import List

from fastapi import APIRouter, Depends

from source.db.client import init_db
from source.depends import get_service
from source.secret.model import Secret
from source.secret.schema import SecretCreate
from source.secret.service import SecretService

router = APIRouter(prefix='/secret', tags=['secret'])


@router.get('/',
            response_model=List[Secret],
            description='get all secrets'
            )
async def get_all_secrets(secret_service: SecretService = Depends(get_service)):
    secrets = await secret_service.get_all_secret()
    return secrets


@router.post('/',
             responses={400: {'description': 'Bad Request'}},
             response_model=SecretCreate,
             description='create secret',
             status_code=201
             )
async def secret_create(secret_data: SecretCreate, secret_service: SecretService = Depends(get_service)):
    return await secret_service.create_secret(secret_data)

#
# @router.get('/{secret_key}')
# async def get_secret(secret_key: str, secret_service: SecretService = Depends(get_secret_service)):
#     return await secret_service.get_secret(secret_key)
