class Solution:
    def search(self, arr, target_sum):
        # arr est sorted donc on regarde r: 0 et l: len(arr) -1
        # si r + l > targer on descend r
        # sinon on augmente l
        # quand les deux pointers ont la meme valeur ont arrete
        # Time: O(n) et O(1) pour memory
        l, r = 0, len(arr) - 1

        while l != r:
            if arr[l] + arr[r] == target_sum:
                return [l, r]

            if arr[l] + arr[r] > target_sum:
                r -= 1
            else:
                l += 1


sol = Solution()
s = sol.search([2, 5, 9, 11], 11)
print(s)
