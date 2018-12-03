def timed(fn):
    from time import perf_counter
    from functools import wraps
    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start

        args_ = [str(a) for a in args]
        kwargs_ = [f"{k} = {v}" for (k, v) in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ",".join(all_args)

        print(f"{fn.__name__} ({args_str}) took {elapsed: .6f} second to run")

        return result

    return inner


# Recursion
# @timed
def calc_recursive_fib(n):
    if n <= 2:
        return 1
    else:
        return calc_recursive_fib(n - 1) + calc_recursive_fib(n - 2)


# print(calc_recursive_fib(6))

@timed
def fib_recursive(n):
    return calc_recursive_fib(n)


# print(fib_recursive(36))

@timed
def fib_loop(n):
    fib_1 = 1
    fib_2 = 1
    for i in range(3, n + 1):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
    return fib_2


from functools import reduce


@timed
def fib_reduce(n):
    initial = (1, 0)
    dummy = range(n)
    fib_n = reduce(lambda prev, n: (prev[0] + prev[1], prev[0]), dummy, initial)
    return fib_n[0]


print(fib_loop(100000))
print(fib_recursive(30))
print(fib_reduce(100000))
