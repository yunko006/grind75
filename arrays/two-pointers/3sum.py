from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                current = n + nums[l] + nums[r]

                if current > 0:
                    r -= 1
                elif current < 0:
                    l += 1

                else:
                    res.append(current)

                    # jusqu'a ici c'est ok pour moi
                    # la c'est les pb :
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res


sol = Solution()
s = sol.threeSum([-1, 0, 1, 2, -1, -4])
print(s)
