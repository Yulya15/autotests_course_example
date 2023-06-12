# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize("test_input, expected", [pytest.param((30, 5, 2), 3, marks=pytest.mark.smoke('smoke')),
                                                  pytest.param((80.5, 5), 16.1, marks=pytest.mark.skip('skipped')),
                                                  ((-30, 6), -5),
                                                  ((99, 0), None),
                                                  (('1', 0), None)])
def test_divisios(test_input, expected):
    try:
        assert all_division(*test_input) == expected
    except(ZeroDivisionError, TypeError) as err:
        assert err



