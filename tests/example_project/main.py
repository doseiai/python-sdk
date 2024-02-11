from dosei_sdk import Dosei

dosei = Dosei()


@dosei.cron_job("* * * * *")
def cron_job():
    _ = None
