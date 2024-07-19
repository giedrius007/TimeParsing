from datetime import datetime, timedelta

import calendar


def add_seconds(start_date_time: datetime, seconds_to_add: int):
    return start_date_time + timedelta(seconds=seconds_to_add)


def add_minutes(start_date_time: datetime, minutes_to_add: int):
    return start_date_time + timedelta(minutes=minutes_to_add)


def add_hours(start_date_time: datetime, hours_to_add: int):
    return start_date_time + timedelta(hours=hours_to_add)


def add_days(start_date_time: datetime, days_to_add: int):
    return start_date_time + timedelta(days=days_to_add)


def add_months(start_date_time: datetime, months_to_add: int):
    # Calculate the year
    year = start_date_time.year + (start_date_time.month + months_to_add - 1) // 12
    # Calculate months
    month = (start_date_time.month + months_to_add - 1) % 12 + 1
    # Calculate days as new month might have fewer days than the previous month
    day = min(start_date_time.day, calendar.monthrange(year, month)[1])

    # Update datetime with new values
    return start_date_time.replace(year, month, day)


def add_years(start_date_time: datetime, years_to_add: int):
    try:
        return start_date_time.replace(year=start_date_time.year + years_to_add)
    except ValueError:
        # If Feb 29th doesn't exist, set to 28th)
        return start_date_time.replace(year=start_date_time.year + years_to_add, day=28)


def snap_years(start_date_time: datetime):
    return snap_months(start_date_time).replace(month=1)


def snap_months(start_date_time: datetime):
    return snap_days(start_date_time).replace(day=1)


def snap_days(start_date_time: datetime):
    return snap_hours(start_date_time).replace(hour=0)


def snap_hours(start_date_time: datetime):
    return snap_minutes(start_date_time).replace(minute=0)


def snap_minutes(start_date_time: datetime):
    return snap_seconds(start_date_time).replace(second=0)


def snap_seconds(start_date_time: datetime):
    return start_date_time.replace(microsecond=0)
