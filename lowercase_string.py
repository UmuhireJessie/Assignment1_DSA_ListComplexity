import timeit
from memory_profiler import profile
import numpy as np
import matplotlib.pyplot as plt


def lowercase_string(string):
   string = string.lower()  #.lower() will turn each character in a string into a lowercase character
   return string


times = []
string = "HJHJGGHRTJGJDsdjsdhsh"
string1 = "HKHHVHKsfsdsdlsdshHGLLGGHHFJJRjfhrujtghHKHVHVKYIFs"
string2 = "jhdliskjdHFGYEEYRJGGFTGFHDJJHGDYRYDGHaudaGGHHTTRYRYUJEHFBidydiaidhaigdaydidagdaduias"
length = [len(string), len(string1), len(string2)]

if __name__ == '__main__':
   times.append(timeit.timeit("lowercase_string(string)", 'from __main__ import lowercase_string, string'))
   times.append(timeit.timeit("lowercase_string(string1)", 'from __main__ import lowercase_string, string1'))
   times.append(timeit.timeit("lowercase_string(string2)", 'from __main__ import lowercase_string, string2'))
print(times)
print(length)
plt.plot(length, times)
plt.xlabel('lengths of strings')
plt.ylabel( 'Average time (ms)')
plt.show()

@profile
def memory_one():     #This is helping us to allocate and find memory space
   space = np.ones(len(string))
   space1 = np.ones(len(string1))
   space2 = np.ones(len(string2))
   spaces = [space, space1, space2]
   return spaces


if __name__ == '__main__':
   memory_one()


def estimation():
   times1 = []
   for i in range(1000000):
       string_estimate = "MwanaFunziihgtehfhgsfeygfb"
       times1.append(timeit.timeit("lowercase_string(string_estimate)", 'from __main__ import lowercase_string, string_estimate'))
       estimated_time = sum(times1) / len(string)
       return string_estimate, estimated_time
