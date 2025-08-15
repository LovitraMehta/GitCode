class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Find the current maximum number of candies any kid has
        max_candies = max(candies)
        
        # Check for each kid if giving them extraCandies makes them reach or exceed max_candies
        return [candy + extraCandies >= max_candies for candy in candies]