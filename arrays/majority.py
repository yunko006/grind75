from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}

        for n in nums:
            if n not in d:
                d[n] = 1
            d[n] += 1

        print(max(d, key=d.get))

    def bayer_moore(self, nums: List[int]) -> int:
        res, count = 0, 0
        for n in nums:
            if count == 0:
                res = n

            count += 1 if n == res else -1
        return res


sol = Solution()
s = sol.majorityElement([2, 2, 1, 1, 1, 2, 2])
print(s)
