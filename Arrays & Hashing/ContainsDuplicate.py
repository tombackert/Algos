# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # O(1)
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)): # O(n)
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT # O(n)