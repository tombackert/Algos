class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert string to lowercase and remove non-alphanumeric characters
        s = ''.join(filter(str.isalnum, s)).lower()
        
        # Check if string is equal to its reverse
        return s == s[::-1]