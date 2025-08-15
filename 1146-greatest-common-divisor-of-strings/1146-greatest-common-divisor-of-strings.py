class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if concatenation in both orders is equal
        if str1 + str2 != str2 + str1:
            return ""
        
        # Helper function to compute GCD of two numbers
        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a
        
        # Get the GCD of the lengths
        gcd_len = gcd(len(str1), len(str2))
        
        # The substring of str1 from 0 to gcd_len is the answer
        return str1[:gcd_len]