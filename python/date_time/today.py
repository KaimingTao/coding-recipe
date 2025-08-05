from datetime import datetime
from datetime import date
from datetime import timedelta


def get_today():
    return date.today()

def get_yesterday():
    return date.today() - timedelta(days=1)
