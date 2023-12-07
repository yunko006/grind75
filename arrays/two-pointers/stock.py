from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Two pointers
        """
        l, r = 0, 1  # left = buy, right = sell
        # 0 et 1 car c'est les index de départ de nos pointers.
        maxP = 0

        while r < len(prices):
            # comment savoir si c'est profitable ?
            if prices[l] < prices[r]:
                # calcul du profit si l < r
                profit = prices[r] - prices[l]
                # compare les 2 max et garde seulement le plus grand.
                maxP = max(maxP, profit)
            else:
                # si le pointer r est plus petit alors on remplace notre l par ce pointer
                l = r
            # on veux toujours incretementer de 1 notre r afin de parcourir tous les index de la list.
            r += 1

        # return le max profit
        return maxP


sol = Solution()
s1 = sol.maxProfit(prices=[7, 1, 5, 3, 6, 4])
print(s1)
print("=" * 80)
s2 = sol.maxProfit([7, 6, 4, 3, 1])
print(s2)
print("=" * 80)
s3 = sol.maxProfit([3, 2, 6, 5, 0, 3])
print(s3)
