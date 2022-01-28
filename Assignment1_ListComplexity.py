# Importing necessary libraries needed to run the program
import random
import timeit
from memory_profiler import profile


# Defining a function of making a random list of values and return a maximum value and using a decorator @profile
# to measure the space or the memory
@profile
def random_list(length):
    list_ = [random.randint(0, number*10) for number in range(length)]
    return f"\nThe random list generated: {list_}\nThe maximum value: {max(list_)}"


# Defining a function that will do the timing as we run the function is executed
def calculating_time(function, *args):
    run_time = timeit.timeit()
    function(*args)
    return run_time


# Defining the main function in order to print the required answer
if __name__ == '__main__':
    print(random_list(10))
    print(f"\nIt takes: {calculating_time(random_list, 10)} seconds to run the function")





