from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # time complexity : O(nlogn) a cause de sorted
        nums = sorted(nums)

        for i, n in enumerate(nums[:-1]):
            if n == nums[i + 1]:
                return True

        return False
