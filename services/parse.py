from functions.dateTime import *
from datetime import datetime, timezone
import re


def parse(command):

    now, date_time_amends, snap = parse_command(command)

    if now:
        return_date_time = datetime.now(timezone.utc)

        # apply all datetime amends
        if date_time_amends:
            for amend in date_time_amends:
                return_date_time = amend_date_time(return_date_time, amend)

        # apply snap
        if snap:
            _, snap_type = snap[0]
            return_date_time = snap_date_time(return_date_time, snap_type)

        return return_date_time


def parse_command(command):
    now = re.findall(r"(now\(\))", command)
    date_time_amends = re.findall(r"(([\+|\-])(\d+)(mon|[smhdy]))", command)
    snap = re.findall(r"(@(mon|[smhdy]))", command)
    return now, date_time_amends, snap


def amend_date_time(current_date_time: datetime, amend_command: tuple):
    _, amend_direction, amend_amount, amend_type = amend_command
    amend_value = int(amend_direction + amend_amount)

    match amend_type:
        case "s":
            return add_seconds(current_date_time, amend_value)
        case "m":
            return add_minutes(current_date_time, amend_value)
        case "h":
            return add_hours(current_date_time, amend_value)
        case "d":
            return add_days(current_date_time, amend_value)
        case "mon":
            return add_months(current_date_time, amend_value)
        case "y":
            return add_years(current_date_time, amend_value)
        case _:
            return current_date_time


def snap_date_time(current_date_time: datetime, snap_type: str):
    match snap_type:
        case "s":
            return snap_seconds(current_date_time)
        case "m":
            return snap_minutes(current_date_time)
        case "h":
            return snap_hours(current_date_time)
        case "d":
            return snap_days(current_date_time)
        case "mon":
            return snap_months(current_date_time)
        case "y":
            return snap_years(current_date_time)
        case _:
            return current_date_time
