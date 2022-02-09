from typing import List

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return twoSum(nums, target)

if __name__ == "__main__":
    print(Solution().twoSum([-3,4,3,90], 0)) 