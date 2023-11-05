'''
Тестирование класса Worker, используя проверочные данные из date_for_test
'''
import unittest

import mane, take_date, date_for_test

date = take_date.take_date()


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.Worker = mane.Worker

    def test_run(self):
        for step in date_for_test.date_for_test:
            a = self.Worker(date=date, request=step[0])
            res_true = step[1]
            self.assertEqual(a.run(), res_true)
