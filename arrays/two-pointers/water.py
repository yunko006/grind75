from typing import List


# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         # two pointers : l, r = 0, 1
#         # current area = 1
#         # quand l < r : l = r et r+=1
#         # quand r =< l : la on calcul current area : min(l ,r) x l - r

#         l, r = 0, 1
#         curr_area = 1
#         max_area = 0
#         while r < len(height):
#             if height[l] < height[r]:
#                 l = r
#                 r += 1
#                 print(l, r)
#             elif height[r] <= height[l]:
#                 print(height[r], height[l])
#                 curr_area = min(height[r], height[l]) * (r - l)
#                 max_area = max(max_area, curr_area)
#                 print(curr_area)
#                 r += 1
#             else:
#                 r += 1

#         return max_area


# # sol = Solution()
# # s = sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
# # print(s)

# # d = sol.maxArea([1, 2, 1])
# # print(d)


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        curr_area = 1
        max_area = 0
        while l < r:
            curr_area = min(height[r], height[l]) * (r - l)
            max_area = max(max_area, curr_area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area


sol = Solution()
s = sol.maxArea([2, 3, 4, 5, 18, 17, 6])

print("=" * 80)
print(s)

d = sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(d)
