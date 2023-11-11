import hashlib

from source.secret.repositories.mongo.mongo import MongoRepository


class SecretService:
    def __init__(self, repository: MongoRepository):
        self.repository = repository

    def get_all_secret(self):
        """
        :return: all secrets
        """
        return self.repository.get_all_secrets()

    def create_secret(self, secret_data: Secret):
        """
        Creates a secret. When creating a Secret, it encrypts the message and hashes the secret key.
        """
        secret = secret_data.model_dump()
        secret['message'] = encode(secret.get('message', ''))
        secret['secret_key'] = hashlib.sha256(secret.get('secret_key', '').encode()).hexdigest()
        return self.repository.create_secret(secret)

    def get_secret(self, secret_key: str):
        """
        Accepts a secret key and returns a message from a document using that secret key
        """
        hash_secret = hashlib.sha256(secret_key.encode()).hexdigest()
        return self.repository.get_secret(hash_secret)
