from datetime import datetime

from loger.loger import get_loger
from source.secret.model import Secret


logger = get_loger('tasks')


async def fetch_expired_ttl() -> None:
    """
    Fetch all expired tasks and delete them
    :return: None
    """
    current_time = datetime.utcnow()
    logger.info(f'fetching expired.. current_time: {current_time}')
    documents = Secret.find(Secret.expireAt <= current_time)
    await documents.delete()
