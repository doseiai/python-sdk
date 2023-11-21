import asyncio
import inspect
import json
import os
import re
from typing import List

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
    cron_jobs: List[CronJob] = []

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
        pattern = re.compile(r'(\w+)\s*=\s*Dosei\(')

        # Convert folder_path to an absolute path
        folder_path = os.path.abspath(folder_path)

        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r') as f:
                        content = f.read()
                        match = pattern.search(content)
                        if match:
                            # Calculate the relative path from folder_path
                            relative_path = os.path.relpath(root, folder_path)

                            # Avoid parent directory references
                            if relative_path.startswith(".."):
                                continue

                            module_path = relative_path.replace(os.sep, '.')
                            module_file = file[:-3]
                            # Handle case where file is in the root of folder_path
                            full_module_path = f"{module_path}.{module_file}" if module_path != '.' else module_file
                            return f"{full_module_path}:{match.group(1)}"

        raise FindDoseiInitError("No Dosei initialization found.")
