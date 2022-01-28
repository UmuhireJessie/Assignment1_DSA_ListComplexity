# importing the memory_profiler module to track the space used
from memory_profiler import profile


# defining a function to track and using a profiler decorator to represent the memory_profiler used to track space
@profile
def simple_function():
    pass


# Defining the main function in order to print the required answer
if __name__ == '__main__':
    simple_function()