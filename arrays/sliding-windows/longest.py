class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = set()
        L = 0
        currentWin = 0
        maxWin = 1

        for R in range(len(s) - 1):
            if s[R] in hashSet:
                maxWin = max(maxWin, len(hashSet))
                hashSet.remove(s[L])
                print(hashSet)
                L += 1

            else:
                hashSet.add(s[R])
                print(hashSet)

        return maxWin


sol = Solution()
s = sol.lengthOfLongestSubstring("abcabcbb")
print(s)
