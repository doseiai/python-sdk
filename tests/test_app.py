import sys

from dosei import Dosei
import pytest

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


def test_apply_app():
    dosei.deploy()
    assert len(dosei.cron_jobs) == 2


def test_find_init():
    init_path = Dosei.find_init("./")
    assert f'{__name__}:dosei' == init_path
