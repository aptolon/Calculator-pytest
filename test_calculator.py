import pytest
from calculator import add, subtract, multiply, divide, power, log, factorial, percentage


def test_add():
    print("Тестируем функцию add...")
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    with pytest.raises(TypeError):
        add(1, 'a')


def test_subtract():
    print("Тестируем функцию subtract...")
    assert subtract(2, 1) == 1
    assert subtract(1, 1) == 0
    with pytest.raises(TypeError):
        subtract(1, 'a')


def test_multiply():
    print("Тестируем функцию multiply...")
    assert multiply(2, 2) == 4
    assert multiply(-1, 1) == -1
    with pytest.raises(TypeError):
        multiply(1, 'a')


def test_divide():
    print("Тестируем функцию divide...")
    assert divide(2, 1) == 2
    assert divide(1, 1) == 1
    with pytest.raises(TypeError):
        divide(1, 'a')
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


def test_power():
    print("Тестируем функцию power...")
    assert power(2, 2) == 4
    assert power(2, 0) == 1
    with pytest.raises(TypeError):
        power(1, 'a')


def test_log():
    print("Тестируем функцию log...")
    assert log(2) == pytest.approx(0.6931471805599453)
    with pytest.raises(TypeError):
        log('a')
    with pytest.raises(ValueError):
        log(0)


def test_factorial():
    print("Тестируем функцию factorial...")
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    with pytest.raises(TypeError):
        factorial('a')
    with pytest.raises(ValueError):
        factorial(-1)


def test_percentage():
    print("Тестируем функцию percentage...")
    assert percentage(2, 100) == 2
    assert percentage(0, 100) == 0
    with pytest.raises(TypeError):
        percentage('a', 100)
