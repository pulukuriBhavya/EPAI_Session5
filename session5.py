import time
import math


def time_it(fn, *args, repetitons= 1, **kwargs):
    total = 0
    if (repetitons < 0):
        raise ValueError("number of repetetions cannot be negative")
    for i in range(repetitons):
        start1 = time.perf_counter()
        fn(*args, **kwargs)
        end1 = time.perf_counter()
        delta1 = end1-start1
        total = total + delta1
    avg = total / repetitons
    #print(avg)
    return avg


def squared_power_list(num, start, end):
    squared_list = []
    if (start < 0 or end < 0):
        raise ValueError("Power should be positive")
    for i in range(start, end):
        squared_list.append(int(math.pow(num, i)))
    #print(squared_list)
    return squared_list


def polygon_area(length, sides):
    if (sides < 0):
        raise ValueError("Sides cannot be negative, should be atleast 3")
    if (length < 0):
        raise ValueError("Length of a polygon cannot be negative")
    if(sides < 3 or sides > 6):
        raise ValueError("Polygon of size 3 to 6 is only accepted")
    #print(sides * (length ** 2) / (4 * math.tan(math.pi / sides)))
    return sides * (length ** 2) / (4 * math.tan(math.pi / sides))


def temp_converter(temp, temp_given_in):
    if (temp < 0):
        raise ValueError("Only positive temperatures should be given")
    if (temp_given_in not in ['f', 'c']):
        raise ValueError("Only Celsius and Farenheit are to be used for conversion")
    if temp_given_in == 'c':
        #print((9 * temp) / 5 + 32)
        return (9 * temp) / 5 + 32
    else:
        #print((temp - 32) * 5 / 9)
        return (temp - 32) * 5 / 9


def speed_converter(speed, dist, time):
    if (speed < 0):
        raise ValueError("Speed cannot be negative")
    if (dist not in ['km', 'm', 'ft', 'yrd'] or time not in ['hr', 'day', 'min', 'sec', 'ms']):
        raise ValueError("Acceptable speed and distance for conversion are "'km', 'm', 'ft', 'yrd'" and "'hr', 'day', 'min', 'sec', 'ms'"")
    dist_dict = {'km': 1, 'm': 1000, 'ft': 3280.84, 'yrd': 1093.613}
    time_dict = {'hr': 1, 'day': 0.041667, 'min': 60, 'sec': 3600, 'ms': 3600000}
    converted_speed = speed * (dist_dict[dist]/time_dict[time])
    #print (converted_speed)
    return (converted_speed)
