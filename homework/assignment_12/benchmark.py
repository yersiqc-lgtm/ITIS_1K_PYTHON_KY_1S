"""
29.10.2026
homework
"""
from time import perf_counter
from recursion import fib, fib_fast

for function in (fib, fib_fast):
    start = perf_counter()
    result = function(30)
    duration = perf_counter() - start
    print(f"{function.__name__}(30) = {result}; time: {duration:.9f} s")
