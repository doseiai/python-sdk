import asyncio
import inspect
import json
import os
from typing import List, Optional

from dosei_util import dosei_util
from croniter import croniter
from pydantic import BaseModel, field_validator


class FindDoseiInitError(Exception):
    pass


class CronJob(BaseModel):
    schedule: str
    entrypoint: str
    is_async: bool

    @field_validator("schedule")
    @classmethod
    def validate_schedule(cls, value):
        if croniter.is_valid(value) is False:
            raise ValueError("Invalid cron schedule format.")
        return value


class Dosei(BaseModel):
    _app_export_path: str = ".dosei/app.json"

    name: Optional[str] = None
    command: Optional[str] = None
    dev: Optional[str] = None
    port: Optional[int] = None
    cron_jobs: Optional[List[CronJob]] = []

    def cron_job(self, schedule: str):

        def decorator(func):
            self.cron_jobs.append(CronJob(
                schedule=schedule,
                entrypoint=f"{func.__module__}:{func.__name__}",
                is_async=Dosei.is_func_async(func)
            ))
            return func

        return decorator

    def export(self):
        os.makedirs(os.path.dirname(self._app_export_path), exist_ok=True)
        with open(self._app_export_path, 'w') as f:
            json.dump(self.model_dump(), f, indent=2)

    @staticmethod
    def is_func_async(func) -> bool:
        return inspect.iscoroutinefunction(func)

    @staticmethod
    def call_func(func):
        is_async = Dosei.is_func_async(func)
        return asyncio.run(func()) if is_async else func()

    @staticmethod
    def find_init(folder_path: str) -> str:
        return dosei_util.find_framework_init("Dosei", folder_path)
