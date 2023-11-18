import asyncio
import inspect
import os
import re


class FindDoseiInitError(Exception):
    pass


class CronJob:

    def __init__(self, schedule: str, func):
        self.schedule = schedule
        self.entrypoint = f"{func.__module__}:{func.__name__}"
        self.is_async = Dosei.is_func_async(func)


class Dosei:

    def __init__(self):
        self.cron_jobs = []

    def cron_job(self, schedule: str):

        def decorator(func):
            self.cron_jobs.append(CronJob(schedule, func))
            return func

        return decorator

    def deploy(self):
        return self

    @staticmethod
    def is_func_async(func) -> bool:
        return inspect.iscoroutinefunction(func)

    @staticmethod
    def call_func(func):
        is_async = Dosei.is_func_async(func)
        return asyncio.run(func()) if is_async else func()

    @staticmethod
    def find_init(folder_path: str) -> str:
        # Regular expression to find Dosei initialization
        pattern = re.compile(r'(\w+)\s*=\s*Dosei\(')

        # Check main.py files first in all subdirectories
        for root, dirs, files in os.walk(folder_path):
            if "main.py" in files:
                with open(os.path.join(root, "main.py"), 'r') as f:
                    content = f.read()
                    match = pattern.search(content)
                    if match:
                        # Convert file path to module path
                        relative_path = os.path.relpath(root, folder_path)
                        module_path = os.path.join(relative_path, "main").replace(os.sep, '.')
                        return f"{module_path}:{match.group(1)}"

        # Check other .py files if no Dosei initialization found in main.py files
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".py") and file != "main.py":
                    with open(os.path.join(root, file), 'r') as f:
                        content = f.read()
                        match = pattern.search(content)
                        if match:
                            # Convert file path to module path
                            relative_path = os.path.relpath(root, folder_path)
                            module_path = os.path.join(relative_path, file[:-3]).replace(os.sep, '.')
                            return f"{module_path}:{match.group(1)}"
        raise FindDoseiInitError("No Dosei initialization found.")
