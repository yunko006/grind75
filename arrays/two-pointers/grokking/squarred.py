class Solution:
    def makeSquares(self, arr):
        squares = [x**2 for x in arr]
        # trouver low
        # l; r = 0, 1
        # TODO: Write your code here
        # idée n1 trouve low avec min(arr)
        # regarder des 2 cotés du zero et append le plus petit
        # chiant a coder
        # idée 2, build la list en partant de la fin
        # l, r = 0, len(arr) - 1

        l, r = 0, len(arr) - 1
        ans = []

        while l <= r:
            if squares[l] <= squares[r]:
                ans.append(squares[r])
                r -= 1
            elif squares[l] > squares[r]:
                ans.append(squares[l])
                l += 1

        return ans[::-1]


sol = Solution()
s = sol.makeSquares([-2, -1, 0, 2, 3])
print(s)
