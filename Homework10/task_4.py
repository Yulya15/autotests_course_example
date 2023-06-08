# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest
import time
import datetime


@pytest.mark.usefixtures('class_with_time')
class Time:

    def test_time_1(self):
        start = datetime.datetime.now()
        time.sleep(3)
        finish = datetime.datetime.now()
        print(f'Начало: {start} Окончание: {finish}')

    def test_time_2(self, lead_time):
        start = datetime.datetime.now()
        time.sleep(2)
        finish = datetime.datetime.now()
        print(f'Время выполнения: {finish - start}')
