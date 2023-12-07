from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        a = sorted(nums)
        print(a)
        # pourquoi on sort ?
        # si on sort on va pouvoir comparer les valeurs tout a gauche et tout a droite
        # si l + r > k alors on bouge r, comme r est tout au bout de la liste on doit enlever 1 pour le faire bouger vers la gauche
        # si l + r < k alors on l, comme l est au tout début de la liste, on doit ajouter 1 pour le faire bouger vers le centre.
        # car il n'y pas d'interet a bouger r vers le centre car la somme ne va faire que dimnuer car o nest dans une array sorted.
        # comme l et r ne peuvent pas egaux, on arrete la loop quand les 2 se rencontrent.
        # time complexity de O(nlogn) a cause de la fonction sorted.
        # pourquoi ans += r - l ?
        l, r = 0, len(a) - 1
        ans = 0
        while l < r:
            print(l, r)
            if a[l] + a[r] < target:
                ans += r - l
                print(ans)
                l += 1
            else:
                r -= 1
        return ans


# Test the function with the provided input
sol = Solution()
output = sol.countPairs(nums=[-6, 2, 5, -2, -7, -1, 3], target=-2)
print(output)
