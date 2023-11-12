from datetime import datetime

from starlette import status
from starlette.responses import JSONResponse

from source.secret.model import Secret
from source.secret.repositories.base import BaseDBManager
from source.secret.schema import SecretCreate
from source.secret.utils import calculate_ttl


class MongoRepository(BaseDBManager):
    async def get_all_secrets(self):
        try:
            secrets = await Secret.find().to_list()
            # serialized_secrets = [secret.model_dump() for secret in secrets]
            return secrets
        except Exception as e:
            return e

    async def create_secret(self, secret_data: dict) -> JSONResponse:
        await Secret(**secret_data).create()
        response_data = {"message": "Secret created successfully"}
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=response_data)

    async def get_secret(self, hash_secret: str) -> str:
        """
        Accepts a secret key and returns a message from a document using that secret key
        """
        secret = await self.db.secret.find_one({'secret_key': hash_secret})
        message = decode(secret.get('message'))
        return message

    async def fetch_expired_ttl(self):
        current_time = datetime.utcnow()
        print(f"Current Time: {current_time}")
        documents = await self.db.secret.find({'expireAt': {'$lt': current_time}}).to_list(length=None)
        print(f"Documents to Delete: {documents}")
        for document in documents:
            await self.db.secret.delete_one({'_id': document['_id']})
            print(f"Deleted document with _id: {document['_id']}")
