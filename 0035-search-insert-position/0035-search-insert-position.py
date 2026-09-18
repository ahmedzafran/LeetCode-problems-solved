class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums.append(target)
        nums = sorted(nums)
        for i,number in enumerate(nums):
            if number == target:
                return i

            