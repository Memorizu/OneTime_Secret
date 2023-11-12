
from source.secret.repositories.mongo.mongo import MongoRepository
from source.secret.service import SecretService


mongo_repository = MongoRepository()
secret_service = SecretService(mongo_repository)


def get_service():
    return secret_service
