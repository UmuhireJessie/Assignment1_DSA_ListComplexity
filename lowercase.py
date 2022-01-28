# Importing necessary libraries needed to run the program
import timeit
from memory_profiler import profile


# Defining a function of making a string to lowercase and return a lowercased string and using a decorator @profile
# # to measure the space or the memory
@profile
def lowercase_string(string):
    lowerString = string.lower()
    return f"The lower cased string is: {lowerString}"


# Defining a function that will do the timing as we run the function is executed
def calculating_time(function, *args):
    run_time = timeit.timeit()
    function(*args)
    return run_time


# Defining the main function in order to print the required answer
if __name__ == '__main__':
    print(lowercase_string("FJR"))
    print(calculating_time(lowercase_string, "FJR"))
