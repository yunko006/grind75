from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        i = 0

        if nums[l] > nums[r]:
            nums[l], nums[r] = nums[r], nums[l]

        print(nums)


sol = Solution()
s = sol.sortColors([2, 0, 2, 1, 1, 1])
