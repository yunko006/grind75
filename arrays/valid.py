from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        open_par = "[{("
        open = []
        closed_par = ")]}"
        closed = []
        valid = True
        for par in s:
            if par in open_par:
                open.append(par)
                print(open)
            elif par in closed_par:
                closed.append(par)
                print(closed)
                if open and closed:
                    if open[-1] == "{" and closed[-1] == "}":
                        print("a")
                        open.pop()
                        closed.pop()
                    elif open[-1] == "(" and closed[-1] == ")":
                        print("b")
                        open.pop()
                        closed.pop()
                    elif open[-1] == "[" and closed[-1] == "]":
                        print("c")
                        open.pop()
                        closed.pop()
                    else:
                        return False
            else:
                return False

        return not open and not closed


# check les par tant que ces des ouvertes pas de soucis, des qu'on rencontre un fermé on check si la last de open est la meme famille.


s = Solution()
sol = s.isValid(s="[[")

print(sol)
