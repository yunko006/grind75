class Solution:
    def remove(self, arr, key):
        i, next = 0, 0

        while i < len(arr):
            if arr[i] != key:
                arr[next] = arr[i]
                next += 1
            i += 1

        return next


sol = Solution()
s = sol.remove([2, 11, 2, 2, 1], 2)
print(s)

d = sol.remove([3, 2, 3, 6, 3, 10, 9, 3], 3)
print(d)
