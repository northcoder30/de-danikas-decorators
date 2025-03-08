from src.convert_type import convert_type

def test_function_call():

    def func():
        convert_type

    expected = None
    assert convert_type(func) == expected


def test_function_take_arg():
    arg1 = 1  
    
    def func(arg):
  # convert_type(arg)

        return arg1 + arg
    
    expected = 2
    assert convert_type(func) == expected
