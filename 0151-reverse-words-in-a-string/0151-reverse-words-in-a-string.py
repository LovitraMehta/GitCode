class Solution:
    def reverseWords(self, s: str) -> str:
        # Split by whitespace and filter out empty strings
        words = s.split()
        # Reverse the list of words
        reversed_words = words[::-1]
        # Join the words with a single space
        return ' '.join(reversed_words)