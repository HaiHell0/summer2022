def fib(n):
    subsolutions = [0] * n  # make a list of size n

    subsolutions[0] = 0
    subsolutions[1] = 1
    for i in range(2, n):  # get subsolutions from 2 to (n-1)
        subsolutions[i] = subsolutions[i-1] + subsolutions[i-2]
    return subsolutions[n-1] + subsolutions[n-2]


if __name__ == "__main__":
    print(fib(100))
