class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        s_list = list(s)  # Convert to list for easy swapping
        left, right = 0, len(s) - 1

        while left < right:
            # Move left pointer until a vowel is found
            while left < right and s_list[left] not in vowels:
                left += 1
            # Move right pointer until a vowel is found
            while left < right and s_list[right] not in vowels:
                right -= 1
            # Swap the vowels
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1

        return ''.join(s_list)