from datetime import datetime

from beanie import Document

from source.secret.schema import LivingTime


class Secret(Document):
    message: str
    secret_key: str
    living_time: LivingTime = LivingTime.ONE_DAY
    created_at: datetime
    expireAt: datetime
