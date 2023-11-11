from datetime import datetime

from starlette import status
from starlette.responses import JSONResponse

from source.secret.repositories.base import BaseDBManager


class MongoRepository(BaseDBManager):

    async def get_all_secrets(self) -> list[Secret]:
        secret_query = self.db.secret.find()
        secrets = await secret_query.to_list(length=10)
        return [Secret(**secret) for secret in secrets]

    async def create_secret(self, secret_data: dict) -> JSONResponse:
        created_at = secret_data.get('created_at', None)
        living_time = secret_data.get('living_time', None)
        secret_data['expireAt'] = calculate_ttl(created_at, living_time)
        await self.db.secret.insert_one(secret_data)
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
