# Write two functions to display the Fibonacci sequence, then write a decorator to compare the execution time of these two functions.

import time

def time_dec(user_function):
    def wrapper(*args,**kwargs):
        print(f"___Before calling {user_function.__name__}")
        s_time = time.time()
        result = user_function(*args,**kwargs)
        e_time = time.time()
        print(f"___After calling{user_function.__name__}")
        print(f"Time span: {(e_time - s_time)*1000} ms\n")
        return result
    return wrapper

@time_dec
def fibo_one(user_length): # iterative
    fibo_list = [0,1]
    def next_number(list):
        return list.append(list[-1]+list[-2])
    for i in range(user_length - 2):
        next_number(fibo_list)
    return fibo_list

def raw_fibo_two(user_length): # recursive
    if user_length <= 1:
        return user_length
    return raw_fibo_two(user_length-1) + raw_fibo_two(user_length-2)
@time_dec
def fibo_two(user_length):
    return raw_fibo_two(user_length)

fibo_one(10000)
fibo_two(30)
