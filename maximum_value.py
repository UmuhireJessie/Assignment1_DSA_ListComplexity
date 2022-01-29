# Importing necessary libraries needed to run the program
import random
import numpy as np
import time
from matplotlib import pyplot as plt


# Defining a function of making a random list of values and return a maximum value
def random_list(length):
    list_ = [random.randint(0, number*10) for number in range(length)]
    return f"\nThe random list generated: {list_}\nThe maximum value: {max(list_)}"


# Defining a function that will do the timing as we run the function is executed
def calculating_time(function, *args):
    start_time = time.time()
    function(*args)
    return time.time() - start_time


# Finding the average time (more accurate time) it takes to run the function. We have used the average time so that we
# can get more accurate time required to execute the function.
def time_computation(number_of_averages,length, function):
    times_spent_on_function = []
    for average in range(number_of_averages):
        times_spent_on_function.append([calculating_time(function, length)])

    # returning the mean or average time spent and change it into ( * 1000) for better approximation
    return np.array(times_spent_on_function).mean(axis=0) * 1000


# Implementing the average times required to execute the function as the length increase and storing those times in a
# variable (average_time_list)
number_of_averages = 5
lengths_of_list = range(1, 101, 49)
average_time_list = np.array([time_computation(number_of_averages, length, random_list) for length in lengths_of_list])

# Plotting the graph of lengths of list with their  time they required
plt.plot(lengths_of_list, average_time_list,'o-', label='change of time with length')
plt.xlabel('lengths of list')
plt.ylabel( 'Average time (ms)')
plt.show()

# Printing the maximum value in a random list generated
print(random_list(10))
print((calculating_time(random_list, 10)))