from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0

        for n in nums:
            curSum = max(curSum, 0)
            curSum += n
            maxSum = max(maxSum, curSum)

        return maxSum


sol = Solution()
s = sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(s)
