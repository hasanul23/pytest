import pytest


def calculate(exp):
    return eval(exp)


@pytest.mark.parametrize("test_input, expected", [("3+5", 8), ("2+4", 6),
                                                  pytest.param("6*9", 42, marks=pytest.mark.xfail)])
def test_calculate(test_input, expected):
    assert calculate(test_input) == expected


@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [2, 3])
def test_foo(x, y):
    pass
