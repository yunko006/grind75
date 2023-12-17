from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        win = set()
        L = 0
        # on bouge la windows quand abs(R - L) > k
        for R in range(len(nums)):
            if abs(R - L) > k:
                win.remove(nums[L])
                L += 1

            if nums[R] in win:
                return True

            win.add(nums[R])

        return False


sol = Solution()
s = sol.containsNearbyDuplicate(nums=[1, 2, 3, 1], k=3)
print(s)
