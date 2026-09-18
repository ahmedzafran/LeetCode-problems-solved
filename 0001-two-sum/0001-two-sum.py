import sys

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for j in range(len(nums)):
            for i in range(len(nums)):
                if i != j:
                    guess_target = nums[j] + nums[i]
                    if target == guess_target:
                        return[j, i]

        