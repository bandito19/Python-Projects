from datetime import datetime
from dataclasses import dataclass


@dataclass
class Habit:
    name: str
    time_since: str
    remaining_days: str
    minutes_saved: float
    money_saved: str


def track_habit(name: str, start:datetime, cost: float, minutes_used: float):
    goal = 60
    hourly_wage: int = 20

    time_elapsed = (datetime.now() - start.total_seconds())
    hours = round(time_elapsed / 60 / 60, 1)
    days = round (hours / 24, 2)

    money_saved = cost * days
    minutes_used = round(days * minutes_used)
    total_money = f'{round(money_saved + (minutes_used / 60 * hourly_wage), 2)}'

    days_togo = round(goal - days)

    remaining_days = 'Cleared' if days_togo <=0 else f'{days_togo}'
    time_since = f'{days} days' if hours > 72 else f'{hours} hours'

    return Habit(name=name, time_since=time_since, remaining_days=remaining_days, minutes_saved=minutes_used, money_saved=total_money)