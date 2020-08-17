import pytest
import inspect
#from test_utils import *
import re
import os.path
import sys

import session5

print_output = "1-2-3 ***\n"
converted_speed = int(69.4444)
converted_temp = 10
area = int(173.20508)
power_list = [4,8,16,32]

def test_fourspace():
    lines = inspect.getsource(session5)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert re.search('[a-zA-Z#@\'\"]', space), "Your code intentation does not follow PEP8 guidelines"
        assert len(re.sub(r'[a-zA-Z#@\n\"\']', '', space)) % 4 == 0, \
        "Your code intentation does not follow PEP8 guidelines"


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session5, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


FUNCTION_CHECK_FOR = [
    'time_it',
    'squared_power_list',
    'polygon_area',
    'temp_converter',
    'speed_converter'
]


def test_functions_avaiable():
    FUNCTIONSAVAILABLE = True
    f = open("session5.py", "r")
    content = f.read()
    f.close()
    for c in FUNCTION_CHECK_FOR:
        if c not in content:
            FUNCTIONSAVAILABLE = False
            pass
    assert FUNCTIONSAVAILABLE == True, "You have not implemented all the functions"


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 400, "Make your README.md file interesting! Add atleast 400 words"



def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_squared_power_input():
    with pytest.raises(ValueError) as e_info:
        r = session5.squared_power_list(2, start=-1, end=5)


def test_polygon_area_sides():
    with pytest.raises(ValueError) as e_info:
        r = session5.polygon_area(length = 15, sides = -2)


def test_polygon_area_length():
    with pytest.raises(ValueError) as e_info:
        r = session5.polygon_area(length = -5, sides = 4)


def test_temp_converter_temp():
    with pytest.raises(ValueError) as e_info:
        r = session5.temp_converter(temp = -100, temp_given_in = 'f')


def test_speed_converter_speed():
    with pytest.raises(ValueError) as e_info:
        r = session5.speed_converter(speed = -50, dist = 'm', time = 'min')


def test_polygon_area_size():
    with pytest.raises(ValueError) as e_info:
        r = session5.polygon_area(length = 15, sides = 1)


def test_temp_converter_input():
    with pytest.raises(ValueError) as e_info:
        r = session5.temp_converter(temp = 100, temp_given_in = 'k')


def test_speed_converter_dist_input():
    with pytest.raises(ValueError) as e_info:
        r = session5.speed_converter(speed = 50, dist = 'mile', time = 'min')
        
        
def test_speed_converter_time_input():
    with pytest.raises(ValueError) as e_info:
        r = session5.speed_converter(speed = 25, dist = 'm', time = 'week')


def test_time_it_input():
    with pytest.raises(ValueError) as e_info:
        r = session5.time_it(session5.squared_power_list, 2, start=0, end=5, repetitons= -20)


def test_time_it_print():
    r = session5.time_it(print, 1, 2, 3, sep='-', end= ' ***\n', repetitons=5)
    assert r != 0, "Your time_it function does not work as intended"


def test_time_it_squared_power_list():
    r = session5.time_it(session5.squared_power_list, 2, start=0, end=5, repetitons=5)
    assert r > 0, "Your time_it function does not work as intended"


def test_time_it_polygon_area():
    r = session5.time_it(session5.polygon_area, 15, sides = 3, repetitons=10)
    assert r > 0, "Your time_it function does not work as intended"



def test_time_it_temp_converter():
    r = session5.time_it(session5.temp_converter, 100, temp_given_in = 'f', repetitons=100)
    assert r > 0, "Your time_it function does not work as intended"


def test_time_it_speed_converter():
    r = session5.time_it(session5.speed_converter, 100, dist='km', time='min', repetitons=200)
    assert r > 0, "Your time_it function does not work as intended"


def test_print():
    sys.stdout = open("print_test.txt", "w")
    print(1, 2, 3, sep='-', end= ' ***\n')
    sys.stdout.close()
    f = open("print_test.txt", "r")
    contents = f.read()
    f.close()
    assert contents == print_output

def test_speed_converter():
    r = int(session5.speed_converter( 250, dist='m', time='sec'))
    assert r == converted_speed, "Your function is not working properly"


def test_temp_converter():
    r = session5.temp_converter(50, temp_given_in = 'f')
    assert r == converted_temp, "Your function is not working properly"


def test_polygon_area():
    r = int(session5.polygon_area(20, sides = 3))
    assert r == area, "Your function is not working properly"


def test_squared_power_list():
    r = session5.squared_power_list(2, start=2, end=6)
    assert r == power_list, "Your function is not working properly"

