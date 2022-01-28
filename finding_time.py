# importing time module to track the time taken to execute the program
import timeit


# defining a function to time
def simple_function():
    pass


# defining a function that will do the timing
def Timing_a_function():
    run_time = timeit.timeit()
    simple_function()
    return run_time


# Defining the main function in order to print the required answer
if __name__ == '__main__':
    print(f"\nIt takes: {Timing_a_function()} seconds to run the function")
