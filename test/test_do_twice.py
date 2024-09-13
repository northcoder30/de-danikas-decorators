from src.do_twice import do_twice

def test_calls_function():
    count = 0
    def test_func():
        nonlocal count
        count += 1
        return count - 1
    expected = 1
    assert do_twice(test_func) == expected

def test_calls_function_twice():
    count = 0
    def test_func():
        nonlocal count
        count += 1
        return count
    expected = 2
    assert do_twice(test_func) == expected