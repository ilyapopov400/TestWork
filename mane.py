import datetime

import take_date, plus_date

REQUEST = {
    "dt_from": "2022-09-01T00:00:00",
    "dt_upto": "2022-12-31T23:59:00",
    "group_type": "month"
}


class Worker:
    def __init__(self, date, request):
        self.date = date  # список для расчета
        self.request = request  # запрос

    def _to_datetime(self, st: str) -> datetime:
        result = datetime.datetime.strptime(st, '%Y-%m-%dT%H:%M:%S')  # преобразование строки из запроса в datetime
        return result

    def _step(self):  # получение объекта NextTime
        duration = self.request.get('group_type')
        step = plus_date.NextTime(name_delta=duration)
        return step

    def _sorted_date(self):  # получим выборку отсортированных дат
        self.dt_from = self._to_datetime(self.request.get('dt_from'))
        self.dt_upto = self._to_datetime(self.request.get('dt_upto'))
        f_sort = lambda x: (x.get('dt') >= self.dt_from and x.get('dt') <= self.dt_upto)
        result = filter(f_sort, self.date)
        return list(result)

    def _list_sort(self, date) -> list:  # список списков отсортированных дат с заданным шагом
        dt_from = self._to_datetime(self.request.get('dt_from'))
        dt_upto = self._to_datetime(self.request.get('dt_upto'))
        result = list()
        while True:
            next_t = self._step()(sourcedate=dt_from)
            if dt_from > dt_upto:
                break
            f_sort = lambda x: (x.get('dt') >= dt_from and x.get('dt') < next_t)  # верхняя граница не входит
            res = list(filter(f_sort, date))
            result.append(res)
            dt_from = next_t
        return result

    def dataset(self):
        dataset = list()
        date_sort = self._sorted_date()
        list_sort = self._list_sort(date=date_sort)
        f_value = lambda x: x.get('value')
        for iter in list_sort:
            dataset_one = sum(map(f_value, iter))
            dataset.append(dataset_one)

        return dataset

    def labels(self):
        dt_from = self._to_datetime(self.request.get('dt_from'))
        dt_upto = self._to_datetime(self.request.get('dt_upto'))
        label = list()
        while True:
            if dt_from > dt_upto:
                break
            data_show = dt_from.strftime('%Y-%m-%dT%H:%M:%S')
            label.append(data_show)
            dt_from = self._step()(sourcedate=dt_from)
        return label

    def run(self):
        dataset = self.dataset()
        label = self.labels()
        result = {
            "dataset": dataset,
            "labels": label
        }
        return result


def mane():
    date = take_date.take_date()  # получили список для расчета

    a = Worker(date=date, request=REQUEST).run()
    print(a)


if __name__ == "__main__":
    mane()
