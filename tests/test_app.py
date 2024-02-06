from dosei import Dosei
import pytest

from dosei.importer import import_from_string

dosei = Dosei()


@dosei.cron_job("* * * * *")
def cron_job():
    _ = None


@dosei.cron_job("* * * * *")
async def async_cron_job():
    _ = None


def test_run_cron_job():
    cron_job()


@pytest.mark.anyio
async def test_async_run_cron_job():
    await async_cron_job()


def test_cron_jobs():
    app: Dosei = import_from_string("tests.test_app:dosei")
    assert len(app.cron_jobs) == 2
