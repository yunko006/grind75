class Solution:
    def remove(self, arr):
        # l, r = 0, 1
        # i = 0
        # si l = r alors r + 1
        # si l!= r alors l = r / r += 1
        # des qu'un chiffre est different on les permute

        non_dup = 1
        # l = current et r = element qui doit pas se repeter
        i = 0
        while i < len(arr):
            if arr[non_dup - 1] != arr[i]:
                arr[non_dup] = arr[i]
                non_dup += 1
            i += 1

            print(arr)
        print(non_dup)


sol = Solution()
s = sol.remove([2, 3, 3, 3, 6, 9, 9])
