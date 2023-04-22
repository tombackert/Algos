# Time Complexity: O(n* k * log(k))
# Space Complexity: O(n)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {} # O(n)
        for s in strs: # O(n)
            sorted_s = ''.join(sorted(s)) # O(k * log(k))
            if sorted_s in anagrams:
                anagrams[sorted_s].append(s)
            else:
                anagrams[sorted_s] = [s]
        return sorted(anagrams.values())