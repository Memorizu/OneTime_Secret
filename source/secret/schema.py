from datetime import datetime
from enum import Enum
from bson import ObjectId
from pydantic import BaseModel, Field


class LivingTime(str, Enum):
    ONE_HOUR = "1 hour"
    THREE_HOURS = "3 hours"
    ONE_DAY = "1 day"
    THREE_DAYS = "3 days"
    ONE_WEEK = "1 week"


class Secret(BaseModel):
    message: str
    secret_key: str
    living_time: LivingTime = LivingTime.ONE_DAY
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class ConfigDict:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
