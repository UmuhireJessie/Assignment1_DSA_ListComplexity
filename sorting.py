import random
import timeit
from memory_profiler import profile


@profile
def random_list(length):
    list_ = [random.randint(0, number*10) for number in range(length)]
    list1 = sorted(list_)
    return list1


def calculating_time(function, *args):
    run_time = timeit.timeit()
    function(*args)
    return run_time


if __name__ == '__main__':
    print(random_list(10))


