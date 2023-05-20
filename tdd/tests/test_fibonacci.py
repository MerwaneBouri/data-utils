from tdd.fibonacci import is_fibonacci_number


def test_fibonacci():
    assert is_fibonacci_number(15) is False
    assert is_fibonacci_number(987) is True
