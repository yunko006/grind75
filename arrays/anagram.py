class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}

        for char in s:
            if not char in d1:
                d1[char] = 1
            d1[char] += 1

        for char in t:
            if not char in d2:
                d2[char] = 1
            d2[char] += 1

        if d1 == d2:
            return True
        else:
            return False


sol = Solution()
s = sol.isAnagram(s="anagram", t="nagaram")
print(s)
