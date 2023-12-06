from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            sub_target = target - n
            # print(sub_target)
            if sub_target in nums[i + 1 :]:
                for j, m in enumerate(nums[i + 1 :]):
                    if sub_target == m:
                        # pk on doit rajouter i ?
                        return [i, i + j + 1]


s = Solution()
sol = s.twoSum(nums=[3, 2, 4], target=6)

print(sol)
