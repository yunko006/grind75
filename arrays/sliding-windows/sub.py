from typing import List


# ca marche mais trop lent pour leetcode.
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # faire des window de k len

        winSum = 0
        L = 0
        res = 0
        for _ in range(len(arr) - k + 1):
            curWin = arr[L : L + k]  # surement tres lent

            # print(curWin)
            L += 1
            # print(sum(arr[:k]))
            if threshold in curWin:
                res += 1
            elif (sum(curWin) / k) >= threshold:
                res += 1

        # print(res)
        return res


sol = Solution()
s = sol.numOfSubarrays(arr=[2, 2, 2, 2, 5, 5, 5, 8], k=3, threshold=4)
print(s)

s1 = sol.numOfSubarrays(arr=[11, 13, 17, 23, 29, 31, 7, 5, 2, 3], k=3, threshold=5)
print(s1)


# need opti


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # faire des window de k len

        res = 0

        for L in range(len(arr) - k + 1):
            curWin = arr[L : L + k]  # surement tres lent
            print(curWin)
            if (sum(curWin) / k) >= threshold:
                res += 1

        return res


sol = Solution()
s = sol.numOfSubarrays(arr=[2, 2, 2, 2, 5, 5, 5, 8], k=3, threshold=4)
print(s)

s1 = sol.numOfSubarrays(arr=[11, 13, 17, 23, 29, 31, 7, 5, 2, 3], k=3, threshold=5)
print(s1)


# solution


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # faire des window de k len
        res = 0
        curSum = sum(arr[: k - 1])

        for L in range(len(arr) - k + 1):
            curSum += arr[L + k - 1]

            if curSum / k >= threshold:
                res += 1
            curSum -= arr[L]

        return res
