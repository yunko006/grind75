
----

# dsa #leetcode

----

# arrays

# [Two-Sum](https://leetcode.com/problems/two-sum/description/)

# twopointers

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums): #1
            sub_target = target - n #2
            for j, m in enumerate(nums[i + 1 :]): #3
                if sub_target == m:#4
                    # pk on doit rajouter i ?
                    return [i, i + j + 1] #5
```

Explications :

# 1

on utilise enumerate pour avoir l'index: i et le chiffre actuel dans la loop: n

# 2 on fait target - n pour savoir si la sub_target est dans la list

# 3

Time complexity :

O(n²)

---

# stacks

# [Valid Parenthesis](https://leetcode.com/problems/valid-parentheses/)

```python
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

            elif par in closed_par:
                closed.append(par)

                if open and closed:

                    if open[-1] == "{" and closed[-1] == "}":
                        open.pop()
                        closed.pop()

                    elif open[-1] == "(" and closed[-1] == ")":
                        open.pop()
                        closed.pop()

                    elif open[-1] == "[" and closed[-1] == "]":
                        open.pop()
                        closed.pop()

                    else:

                        return False

            else:

                return False

  

        return not open and not closed
```

Explications :

Time complexity :

O(n) a cause de la for loop.

----

# Best time to buy and sell stock

# arrays #twopointers

Utiliser Two Pointers pour suivre les jours (le temps) : Left et Right (L et R)
L = Buy
R = Sell

update le left pointer uniquement si un chiffre a droite est plus petit, exemple :
1, 3,4,5 on update jamais notre left pointer mais si 2,3,1,5, au début L = 2 puis quand on rencontre le 1 on update notre left pour L = 1

il faut aussi tracker le current max profit et prendre celui a le plus gros chiffre.

**Time complexity** : O(n) car on parcours la list qu'une seule fois.

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Two pointers
        """
        l, r = 0, 1  # left = buy, right = sell
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
```

---

# arrays #twopointers

# [Count Pairs Whose Sum is Less than Target](https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/)

```python
class Solution:

    def countPairs(self, nums: List[int], target: int) -> int:
        a = sorted(nums) # O(nlogn)
        l, r = 0, len(a) - 1
        ans = 0

        while l < r: #O(n)

            if a[l] + a[r] < target:
                ans += r - l
                l += 1
            else:
                r -= 1

        return ans
```

pourquoi on sort ?

- si on sort on va pouvoir comparer les valeurs tout a gauche et tout a droite

- si l + r > k alors on bouge r, comme r est tout au bout de la liste on doit enlever 1 pour le faire bouger vers la gauche

- si l + r < k alors on l, comme l est au tout début de la liste, on doit ajouter 1 pour le faire bouger vers le centre.
  car il n'y pas d'intérêt a bouger r vers le centre car la somme ne va faire que diminuer car on est dans une array sorted.

- comme l et r ne peuvent pas égaux, on arrête la loop quand les 2 se rencontrent.
- time complexity de O(nlogn) a cause de la fonction sorted.

Pourquoi ans += r - l ?

- When the sum is less than the target, we know there are R-L pairs which sum less than target

Exemple avec a = [-7, -6, -2, -1, 2, 3, 5]
-7 + 5 = -2 : on passe donc on bouge a gauche
-6 + 5 = -1 < -2 donc la comme on sait que la liste est rangé dans l'ordre ca veux dire que toutes les valeurs qui sont entre -6 et 5 vont etre des pairs qui sont < -2 car si on reduit notre R on a : -6 + 3 = -3 < -2 etc donc c'est pour cela qu'on fait R - L.

---

# arrays #leetcode #hashmap

# [Majority Element](https://leetcode.com/problems/majority-element/)

## Solution 1 : Hash map

```python
def hash_map_solution(self, nums) -> int:
d = {}
 for n in nums:
  if not d[n]:
   d[n] = 1
  else:
   d[n] += 1
 return max(d, key.get)
```

Explications :
ez

## Solution 2 : Bayer-Moore algo

Cette algo se base sur le fait qu'il y ait forcement un valeur qui apparaissent plus souvent, d'apres la description du probleme on sait que la valeur va apparaitre au moins n/2 fois
par exemple si len(list) = 7 alors notre value va apparaitre au moins 4 fois.

```python
def bayer_moore(self, nums: List[int]) -> int:
        res, count = 0, 0
        for n in nums:
            if count == 0:
                res = n

            count += 1 if n == res else -1
            
        return res
```

Explications :

- on initialise res (resultat) et count à 0
- on parcours nums, si le count == 0 alors on change le resultat par la valeur de n actuelle.
- sinon, on ajoute 1 a count si res et n sont les egaux, sinon on soustrait 1.

*Exemple pour mieux comprendre :

list = [2,1,1,3,3,1,1]

1: count == 0 donc res = 2 , on ajoute 1 a count donc count == 1
2 : count != 0, mais res !=n donc on enleve 1 a count donc count == 0
3: count == 0, donc res = 1, res == n donc count += 1
4: count !=0, res !=n donc count -= 1 donc count = 0
5: count == 0, donc res = 3, res == n donc count += 1
6: count != 0, res != n donc count -= 1 donc count = 0
7: count == 0 donc res = 1, res == n donc count += 1 donc count =1
Itérations finis donc res = 1

---

# arrays #leetcode

# [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #time complexity : O(nlogn) a cause de sorted
        nums = sorted(nums)
        for i, n in enumerate(nums[:-1]):
        
            if n == nums[i+1]:
                return True

        return False
```

on sort la list comme ca tous les nombres sont bien placés, puis on regarde si 2 nombres cote a cote sont egaux si ou

---

# arrays #leetcode

# [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

# twopointers

1. on lower le string
2. on initialise les two pointers
3. objectif de check si le debut et la fin sont egaux exemple index 0 avec index -1, idx 1 avec idx -2 etc etc
4. si index de gauche n'est pas un char aplh on bouge notre pointeur pour pouvoir comparer
5. meme chose pour la droite
6. si a un moment les deux sont pas egaux on return False
7. si egaux alors on bouge nos deux pointers pour continuer dans le string
8. on return true si while loop fini.

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l, r = 0, len(s) - 1
        
        while l < r:
            if not s[l].isalnum():
                l += 1

            elif not s[r].isalnum():
                r -= 1

            elif s[l] != s[r]:
                return False

            else:
                l += 1
                r -= 1

        return True
```

---

---

# 3Sum

![[Pasted image 20231214162216.png]]

sum > 0 : r -=1
sum < 0 : l += 1

enfaite l'idée c'est de sort la liste avec la built in fonction : sorted donc O(nlogn)

ensuite comme la liste est sorted on va pouvoir reutiliser le principe de two sum 2 : regarder les index de début et de fin.

mais avant de faire ca il faut faire une premiere loop pour prendre en compte le numéro actuel de la for loop genre -3
on aurait n = -3 (for i, n in enumerate(nums)) et l = i + 1 et r = len(nums) - 1
pk l = i + 1 ? car on veux faire n + (n+1) + n[-1]
disons que n + (n+1) + n[-1]  = current

si current > 0 alors on descend le pointer r comme dans two sum two
si current < 0 alors on monte le pointer l

else current = 0 et on append notre list dans notre list ans

le probleme survient a cause de l'énoncé qui dit qu'on ne doit pas avoir 2 fois la meme liste dans notre liste res
il faut donc falloir check si les chifffres apres notre n actuel sont egaux a n

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue
                
            l, r = i + 1, len(nums) - 1
            while l < r:
                current = n + nums[l] + nums[r]
                
                if current > 0:
                    r -= 1
                    
                elif current < 0:
                    l += 1
                    
                else:
                    res.append(current)
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return res
```

---

# [Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

# twopointers

il faut partir a l'envers car c''est plus simple de calculer l'area d'un rectangle.

idée :

calculer area avec :

```python
curr_area = min(height[r], height[l]) * (r - l)
max_area = max(max_area, curr_area)
```

pk ? car on prends toujours la hauteur minimal entre l et r et on fait * (r - l ) pour avoir le calcul d'une aire d'un rectangle

quand l < r on deplace l : l +=1 car au début de la liste.

quand l>= r on deplace r : r -=1 car r est au bout de la liste.

```python
class Solution:

    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        curr_area = 1
        max_area = 0

        while l < r:
            curr_area = min(height[r], height[l]) * (r - l)
            max_area = max(max_area, curr_area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return max_area
```

---

# [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)

# twopointers
