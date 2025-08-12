from datetime import datetime

def get_week_between(date1, date2):

    date1 = datetime.strptime(date1, "%Y-%m-%d").date()
    date2 = datetime.strptime(date2, "%Y-%m-%d").date()

    days_diff = abs((date2 - date1).days)
    weeks_diff = days_diff / 7

    return weeks_diff
