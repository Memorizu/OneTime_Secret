from datetime import datetime

from source.secret.model import Secret


async def fetch_expired_ttl():
    current_time = datetime.utcnow()
    print(f"Current Time: {current_time}")
    documents = Secret.find(Secret.expireAt <= current_time)
    await documents.delete()
