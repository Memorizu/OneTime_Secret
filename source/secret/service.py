import hashlib
from typing import Any, Coroutine

from source.secret.repositories.base import BaseDBManager
from source.secret.schema import SecretCreate
from source.secret.utils import calculate_ttl, encode


class SecretService:
    def __init__(self, repository: BaseDBManager):
        self.repository = repository

    def get_all_secret(self) -> Coroutine[Any, Any, Any]:
        """
        :return: all secrets
        """
        return self.repository.get_all_secrets()

    def create_secret(self, secret_data: SecretCreate) -> Coroutine[Any, Any, Any]:
        """
        Creates a secret. When creating a Secret, it encrypts the message and hashes the test_secret key.
        """
        secret = secret_data.model_dump()
        secret['message'] = encode(secret.get('message', ''))
        secret['secret_key'] = hashlib.sha256(secret.get('secret_key', '').encode()).hexdigest()
        created_at = secret.get('created_at', None)
        living_time = secret.get('living_time', None)
        secret['expireAt'] = calculate_ttl(created_at, living_time)
        return self.repository.create_secret(secret)

    def get_secret(self, secret_key: str) -> Coroutine[Any, Any, Any]:
        """
        Accepts a test_secret key and returns a message from a document using that test_secret key
        """
        hash_secret = hashlib.sha256(secret_key.encode()).hexdigest()
        return self.repository.get_secret(hash_secret)
