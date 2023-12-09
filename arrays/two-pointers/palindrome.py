from typing import List


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1 remove non alpha numeric et lower
        s = s.lower()
        l, r = 0, len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l] != s[r]:
                return False
            # print(f"gauche: {s[l]}, droite {s[r]}")
            else:
                l += 1
                r -= 1

        return True


sol = Solution()
s = sol.isPalindrome("A man, a plan, a canal: Panama")
print(s)
