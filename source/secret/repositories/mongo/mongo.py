
from starlette import status
from starlette.responses import JSONResponse

from source.secret.model import Secret
from source.secret.repositories.base import BaseDBManager
from source.secret.utils import decode


class MongoRepository(BaseDBManager):
    async def get_all_secrets(self) -> list[Secret]:
        secrets = await Secret.find().to_list()
        return secrets

    async def create_secret(self, secret_data: dict) -> JSONResponse:
        await Secret(**secret_data).create()
        response_data = {"message": "Secret created successfully"}
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=response_data)

    async def get_secret(self, hash_secret: str) -> str | None:
        """
        Accepts a test_secret key and returns a message from a document using that test_secret key
        """
        try:
            secret = await Secret.find_one({'secret_key': hash_secret})
            message = decode(secret.message)
            return message
        except AttributeError:
            return None
