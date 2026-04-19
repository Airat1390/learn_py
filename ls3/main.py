import time
import functools

def trace (func):
    trace.depth = 0

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        indent = " " * trace.depth
        print(f"{indent}--> Вход в {func.__name__}({args[0]}")

        trace.depth +- 1
        result = func(*args, **kwargs)
        trace.depth -= 1

        print(f"{indent}<-- Выход из {func.__name__}({args[0]}) = {result}")
        return result
    return wrapper


def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Функция {func.__name__} выполнилась за {execution_time:.4f} сек.")

        return result
    return wrapper

@timer_decorator
def pow (inpute_list):
    degree = int(input("Выберете и введите число для возведение в выбранную вами степень: "))
    for item in inpute_list:
        print(item ** degree)
        

@timer_decorator
def even_and_odd (inpute_list):
    for item in inpute_list:
        if item % 2 == 0:
            print(f"{item}, Число четное")
        else:
            print(f"{item}, Число нечетное")

@trace
def fibonachi (num):
#    if num <= 0: return 0
#    if num == 1: return 1
#
#    prev = 0
#    now  = 1
#
#    for _ in range(num - 1):
#        next = prev + now
#        prev = now
#        now = next
#
#    return now

    if num <= 1:
        return num
     
    return fibonachi(num - 1) + fibonachi(num - 2)  
        


arr1 = [2, 5, 10, 15, 20]
pow(arr1)

arr2 = [10, 11, 12, 15, 16, 17, 18, 19, 20]
even_and_odd(arr2)

print(fibonachi(22))



