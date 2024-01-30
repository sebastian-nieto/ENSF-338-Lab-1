import timeit
import math

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
    
#chat-gpt was used for this line
time_recursive = timeit.timeit(lambda: fact(100), number=10000)

def for_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

#chat-gpt was used for this line
time_for_loop = timeit.timeit(lambda: for_loop(100), number=1000)

#chat-gpt was used for this function
def list_comprehension(n):
    return math.prod(range(1, n + 1))

time_list_comprehension = timeit.timeit(lambda: list_comprehension(100), number = 1000 )



print(f"Time for recursive {time_recursive}, time for for loop {time_for_loop}, time for list comprehension {time_list_comprehension}")