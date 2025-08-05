from datetime import datetime
from typing import AnyStr


DATE_FORMAT_LIST = [
    '%B %Y',
    '%B %d, %Y',
    '%Y-%m-%d',
    '%d/%m/%Y',
    '%d-%m-%Y',
    '%d %m %Y',
]


def parse_date(datetime_str, format='%Y-%m-%d'):
    return datetime.strptime(datetime_str, format)


def try_parse_date(date: AnyStr):
    for format in DATE_FORMAT_LIST:
        try:
            date = datetime.strptime(date, format)
            break
        except ValueError:
            continue

    return date
