def f(nums):
    size = len(nums)
    if size == 0:
        return 0
    if size == 1:
        return nums[0]

    return f0(nums, len(nums)-1)


cache = {}


def f0(nums, n):
    if n in cache:
        return cache[n]
    else:
        if n == 0:
            result = nums[0]
        elif n == 1:
            result = max(nums[0], nums[1])
        else:
            result = max(nums[n] + f0(nums, n - 2), f0(nums, n - 1))

    cache[n] = result
    return result


if __name__ == "__main__":
    print(f([1, 1]))
    print(f([2, 7, 9, 3, 1]))
    print(f([1, 7, 9, 5, 1, 3, 4]))
