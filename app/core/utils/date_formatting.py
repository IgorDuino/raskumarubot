from datetime import datetime


def format_date(date_to_format: datetime):
    return date_to_format.strftime("%Y-%m-%d %H:%M:%S")
