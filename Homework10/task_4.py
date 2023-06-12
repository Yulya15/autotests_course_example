# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.
import pytest


@pytest.mark.usefixtures("start_end_time")
class TestDiv:
    """
    Класс с фикстурой, которая печатает время начала выполнения и окончания тестов
    """
    def all_division(*arg1):
        division = arg1[1]
        for i in arg1[2:]:
            division /= i
        return division

    def test_positive_1(self):
        assert self.all_division(30, 5, 2) == 3, 'Неверный результат деления трех целых чисел'

    def test_positive_2(self):
        assert self.all_division(80.5, 5) == 16.1, 'Неверный результат деления числа с плавающей точкой на целое число'

    def test_positive_3(self):
        assert self.all_division(-30, 6) == -5, 'Неверный результат деления отрицательного числа на положительное'

    def test_div_zero(self):
        with pytest.raises(ZeroDivisionError):
            self.all_division(10, 0)

    def test_not_digit(self, work_time):
        """
        Функция с фикстурой, которая считает время выполнения теста
        """
        with pytest.raises(TypeError):
            self.all_division('1', 0)