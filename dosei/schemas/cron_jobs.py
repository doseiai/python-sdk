import uuid
from datetime import datetime

from croniter import croniter

from pydantic import BaseModel, Field, field_validator


class CronJob(BaseModel):
    id: str = Field(default_factory=lambda: uuid.uuid4().__str__().replace("-", ""))
    schedule: str
    entrypoint: str
    owner_id: str
    project_id: str
    deployment_id: str

    updated_at: datetime = Field(default_factory=lambda: datetime.now())
    """datetime: The timestamp when the deployment was last updated."""

    created_at: datetime = Field(default_factory=lambda: datetime.now())
    """datetime: The timestamp when the deployment was created."""

    @field_validator("schedule")
    @classmethod
    def validate_schedule(cls, value):
        if croniter.is_valid(value) is False:
            raise ValueError("Invalid cron schedule format.")
        return value
