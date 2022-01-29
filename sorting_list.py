from multiprocessing.dummy import freeze_support
import random
import matplotlib.pyplot as plt


# Defining a function to accept and take a list.
def sorting_list(list1):
    list1.sort()
    return list1


# Passing three different lists with different lengths
list1 = [10, 9, 4, 28, 7, 40, 12]
list2 = [random.randint(1, 100) for i in range(50)]
list3 = [random.randint(1, 100) for i in range(90)]
sorting_time = []

# A method to calculate the time taken to sort a list
if __name__ == '__main__':
    sorting_list(list1)
    import timeit

    print("The time taken by the algorithm to run is:")
    sorting_time.append(timeit.timeit("sorting_list(list1)", setup="from __main__ import sorting_list,list1"))
    sorting_time.append(timeit.timeit("sorting_list(list2)", setup="from __main__ import sorting_list,list2"))
    sorting_time.append(timeit.timeit("sorting_list(list3)", setup="from __main__ import sorting_list,list3"))
    print(sorting_time)
    # Plotting the time and space taken by each list.
plt.plot(sorting_time)
plt.xlabel('lengths of list')
plt.ylabel( 'Average time (ms)')
plt.show()
# A method for profiling the memory
from memory_profiler import memory_usage

if __name__ == '__main__':
    freeze_support()
    memory_space = memory_usage((sorting_list, [list1]))
    print(memory_space)


def estimate(number_of_averages, length, function):
    times_spent_on_function = []
    for average in range(number_of_averages):
        timeit.timeit()
        function(length)
        times_spent_on_function.append([timeit.timeit])

    estimation_time = sum(times_spent_on_function) / len(times_spent_on_function)
    return estimation_time