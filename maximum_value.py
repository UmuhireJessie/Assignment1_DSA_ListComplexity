# Importing necessary libraries needed to run the program
import random
import numpy as np
import timeit
from matplotlib import pyplot as plt
from memory_profiler import profile


# Defining a function of making a random list of values and return a maximum value
def random_list(length):
    list_ = [random.randint(0, number*10) for number in range(length)]
    return f"\nThe random list generated: {list_}\nThe maximum value: {max(list_)}"


# Defining a function that will do the timing as we run the function is executed
def calculating_time(function, *args):
    runTime = timeit.timeit()
    function(*args)
    return runTime


# Implementing the times required to execute the function as the length increase and storing those times in a
# variable (average_time_list)
lengths_of_list = range(1, 101, 49)
average_time_list = np.array([calculating_time(random_list, length) for length in lengths_of_list])

# Plotting the graph of lengths of list with their  time they required
plt.plot(lengths_of_list, average_time_list,'o-', label='change of time with length')
plt.xlabel('lengths of list')
plt.ylabel('Average time (ms)')
plt.show()

# Printing the maximum value in a random list generated and adding a decoration to it to measure the space
@profile
def printing_result():
    print(random_list(10))


printing_result()