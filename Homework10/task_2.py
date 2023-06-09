# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke
def test_positive_1():
    assert all_division(30, 5, 2) == 3, 'Неверный результат деления трех целых чисел'


def test_positive_2():
    assert all_division(80.5, 5) == 16.1, 'Неверный результат деления числа с плавающей точкой на целое число'


def test_positive_3():
    assert all_division(-30, 6) == -5, 'Неверный результат деления отрицательного числа на положительное'


@pytest.mark.zero
def test_div_zero():
    with pytest.raises(ZeroDivisionError):
        all_division(10, 0)


@pytest.mark.smoke
def test_not_digit():
    with pytest.raises(TypeError):
        all_division('1', 0)

