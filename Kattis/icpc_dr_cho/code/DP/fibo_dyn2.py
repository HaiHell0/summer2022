subsolutions = {}  # empty dictionary to store key/values
subsolutions[0] = 0
subsolutions[1] = 1


def fib(n):
    if n in subsolutions:  # we already have the result
        return subsolutions[n]
    else:
        result = fib(n-1) + fib(n-2)
        subsolutions[n] = result  # memoization
        return subsolutions[n]


if __name__ == "__main__":
    print(fib(100))
