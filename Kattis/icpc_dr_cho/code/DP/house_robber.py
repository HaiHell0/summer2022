# f(n) =  Largest amount that you can rob from first house to nth indexed house.
# Ai = Amount of money at the ith index house.
# f(n) = An + f(n-2) <- When we select the last one
# f(n) = f(n) = f(n-1) <- When not
# f(n) = max(An + f(n-2), f(n-2))
# F(0) = A0
# f(1) = max(A0, A1)
# This is recursive formula

def f(nums):
    size = len(nums)
    if size == 0:
        return 0
    if size == 1:
        return nums[0]

    A = [0] * size

    for (index, value) in enumerate(nums):
        if index == 0:
            A[0] = value
        elif index == 1:
            A[1] = max(A[0], value)
        else:
            A[index] = max(value + A[index - 2], A[index - 1])

    return A[-1]


if __name__ == "__main__":
    print(f([1, 1]))
    print(f([2, 7, 9, 3, 1]))
    print(f([1, 7, 9, 5, 1, 3, 4]))
