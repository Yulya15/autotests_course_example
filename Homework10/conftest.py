# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest
import datetime


@pytest.fixture(scope="class")
def start_end_time():
    start = datetime.datetime.now()
    yield
    finish = datetime.datetime.now()
    print(f'Начало: {start}, Окончание: {finish}')


@pytest.fixture()
def work_time():
    start = datetime.datetime.now()
    yield
    finish = datetime.datetime.now()
    print(f'\nВремя выполнения: {finish - start}')

