from abc import abstractmethod


class BaseDBManager(object):
    @abstractmethod
    async def get_all_secrets(self):
        pass

    @abstractmethod
    async def create_secret(self, secret_data: dict):
        pass

    @abstractmethod
    async def get_secret(self, hash_secret: str):
        pass
