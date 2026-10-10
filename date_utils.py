
from datetime import date


WEEKDAYS = [
    "понедельник",
    "вторник",
    "среда",
    "четверг",
    "пятница",
    "суббота",
    "воскресенье",
]


def parse_date(date_string):
    """Преобразует строку формата ГГГГ-ММ-ДД в дату."""
    return date.fromisoformat(date_string)


def days_between(date1, date2):
    """Возвращает количество дней между двумя датами."""
    first = parse_date(date1)
    second = parse_date(date2)
    return abs((second - first).days)


def weekday_name(date_string):
    """Определяет день недели по заданной дате."""
    parsed_date = parse_date(date_string)
    return WEEKDAYS[parsed_date.weekday()]


def is_leap_year(year):
    """Проверяет, является ли год високосным."""
    return year % 4 == 0


def days_until_new_year(date_string):
    """Вычисляет количество дней до следующего 1 января."""
    current_date = parse_date(date_string)
    next_new_year = date(current_date.year + 1, 1, 1)
    return (next_new_year - current_date).days
