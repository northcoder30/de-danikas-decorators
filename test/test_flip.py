from src.flip import flip

def test_invokes_given_func():
    count = 0
    def input_func(*args):
        nonlocal count
        count += 1
    flipped_func = flip(input_func)
    flipped_func(1, 2)

    assert count == 1

def test_that_func_takes_two_args():
    def input_func(arg1, arg2):
        return arg1 - arg2 
    flipped_func = flip(input_func)
    expected1 = -2

    assert flipped_func(3, 1) == expected1

def test_flips_divide_func():
    a = 10
    b = 2
    def test_divide(a, b):
        return a/b
    flipped_func = flip(test_divide)
    expected = 0.2
    assert flipped_func(a,b) == expected

def test_with_strs():
    a = "cat"
    b = "dog"
    def test_func(a, b):
        return a+b
    flipped_func = flip(test_func)
    expected = "dogcat"
    assert flipped_func(a,b) == expected
