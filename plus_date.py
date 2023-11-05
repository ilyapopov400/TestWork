import datetime, calendar


class NextTime:
    '''
    передаем str: hour, day, month, получаем объект класса.
    При его вызове (передаем текущую дату и количество шагов), получаем дату
    '''

    def __init__(self, name_delta: str):
        self.name_delta = name_delta

    def _add_months(self, sourcedate: datetime, months: int) -> datetime:
        month = sourcedate.month - 1 + months
        year = sourcedate.year + month // 12
        month = month % 12 + 1
        hour = sourcedate.hour
        minute = sourcedate.minute
        second = sourcedate.second
        day = min(sourcedate.day, calendar.monthrange(year, month)[1])
        return datetime.datetime(year, month, day, hour, minute, second)

    def _add_weeks(self, sourcedate: datetime, weeks: int):
        timedelta = datetime.timedelta(days=weeks * 7)
        result = sourcedate + timedelta
        return result

    def _add_days(self, sourcedate: datetime, days: int):
        timedelta = datetime.timedelta(days=days)
        result = sourcedate + timedelta
        return result

    def _add_hours(self, sourcedate: datetime, hours: int):
        timedelta = datetime.timedelta(hours=hours)
        result = sourcedate + timedelta
        return result

    def __call__(self, sourcedate: datetime, step=1):
        result_dc = {
            'month': self._add_months,
            'week': self._add_weeks,
            'day': self._add_days,
            'hour': self._add_hours,
        }
        result = result_dc.get(self.name_delta)
        return result(sourcedate, step)
