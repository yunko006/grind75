from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        marche po atm.
        """
        # que des sub array donc forcement nombre tel que 0 et 1
        l, r = 0, 1
        ans = 0
        res = max(nums)
        # print(len(nums))
        while r < len(nums):
            temp = 0

            if ans == 0:
                ans += nums[l] * nums[r]

            temp += nums[l] * nums[r]
            print(f"{nums[l]} x {nums[r]} = {temp}")

            if temp > ans:
                ans = temp

            l += 1
            r += 1
        print(ans)
        if ans < res:
            return res

        return ans


sol = Solution()
s = sol.maxProduct([-2, 3, -4])
print(s)
