# session5-pulukuriBhavya
Session 5 is concentarted on **Functional Parameters**
***
- **Functional Parameters** consists of **Positional Arguments** and **Keyword Arguments**


## Getting Started
***
These instructions will get you a copy of the project up and running on your local machine for development and testing purpose.

### Prerequisites
***
Before string session check if all the required packages (pytest) are installed. Packages can be installed using the following code.
```
 pip install pytest
 ```

### Session 5.py
***

Session5.py helps getting hands on concepts of Functional Parameters.

- time_it() function calculates the average time taken to run a function. Input parameters for time_it() function are function_name (to be called), *args(parameters of the function 'function_name'), repetitions (number of time the function needs to be called), **Kwargs(parameters of the function 'function_name' )
- squared_power_list() function returns a list constiting of numbers raised to the power of given range. Input parameters for squared_power_list() function are num(number to be raised to the power), start (start of range of power), end( end of range of power).
- polygon_area() function returns the area of given polygon. Input parameters for polygon_area() function are length(length of side of polygon),sides (number of sides to polygon)
- temp_converter() function returns the temperature after converting. Input parameters for temp_converter() function are temperature, temp_given_in (temperature given in 'c' or 'f')
- speed_converter() function returns the speed after conversion. Input parameters for speed_converter() function are speed, dist, time. 

### test_session5.py

***

test_session5.py consists of 26 test cases which needs to be cleared.

- test_fourspace to check for indentation.
- test_function_name_had_cap_letter function name having capital letter.
- test_functions_avaiable to check if all the functions are implemeted.
- test_readme_exists to check if the README file exists
- test_readme_contents to check if the README content is exceding 400 words
- test_readme_file_for_formatting() to check for proper formatting
- test_squared_power_input checks for negative values of power
- test_polygon_area_sides checks for negative values for sides
- test_polygon_area_length checks for negative values for length
- test_temp_converter_temp checks for negative values of temperature
- test_speed_converter_speed checks for negative values of speed
- test_polygon_area_size checks for range of sides
- test_temp_converter_input checks for temperature modes other tha 'c', 'f'
- test_speed_converter_dist_input checks for modes of distance
- test_speed_converter_time_input checks for modes of time 
- test_time_it_input checks for negative repetitions 
- test_time_it_print checks time_it function by passing print function
- test_time_it_squared_power_list checks time_it function by passing squared_power_list function
- test_time_it_polygon_area checks time_it function by passing polygon_area function
- test_time_it_temp_converter checks time_it function by passing temp_converter function
- test_time_it_speed_converter checks time_it function by passing speed_converter function
- test_speed_converter checks if the function returns correct converted speed
- test_temp_converter checks if the function returns correct converted temperature
- test_polygon_area checks if the function returns area of polygon calculated correctly
- test_squared_power_list checks if the function returns squared poer list