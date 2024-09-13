from src.once import once

def test_return_none():
    def func():
        pass
    expected = None
    assert once(func) == expected

def test_function_called_once():
    count = 0
    def func():
        nonlocal count
        count += 1
        return "Would you look at that, I've been invoked!"
    expected = "Would you look at that, I've been invoked!"
    # expected = 1
    assert once(func) == expected

def test_function_not_allowed_repeat():
    count = 0
    def func():
        nonlocal count
        count += 1
        if count == 1:
            return "Would you look at that, I've been invoked!"
        return None
    expected = "Would you look at that, I've been invoked!"
    assert once(func) == expected
    assert once(func) == None
    assert once(func) == None
