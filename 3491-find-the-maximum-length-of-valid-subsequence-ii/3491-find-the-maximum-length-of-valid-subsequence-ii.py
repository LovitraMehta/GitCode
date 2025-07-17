from typing import List

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0

        for val in range(k):
            dp = [0] * k  # dp[r] = max length ending with residue r
            for num in nums:
                r = num % k
                s = (k + val - r) % k  # required previous residue
                candidate = dp[s] + 1 if dp[s] > 0 else 1
                dp[r] = max(dp[r], candidate)
                ans = max(ans, dp[r])

        return ans