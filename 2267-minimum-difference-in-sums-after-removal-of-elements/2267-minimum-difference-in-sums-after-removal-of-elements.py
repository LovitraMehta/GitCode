from heapq import heappush, heappop

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        left_sum = [0] * len(nums)
        right_sum = [0] * len(nums)

        # Maximize sum of smallest n values in the first 2n elements
        max_heap = []
        total = sum(nums[:n])
        for i in range(n):
            heappush(max_heap, -nums[i])
        left_sum[n - 1] = total

        for i in range(n, 2 * n):
            heappush(max_heap, -nums[i])
            total += nums[i] + heappop(max_heap)
            left_sum[i] = total

        # Minimize sum of largest n values in the last 2n elements
        min_heap = []
        total = sum(nums[-n:])
        for i in range(3 * n - 1, 3 * n - n - 1, -1):
            heappush(min_heap, nums[i])
        right_sum[2 * n] = total

        for i in range(2 * n - 1, n - 1, -1):
            heappush(min_heap, nums[i])
            total += nums[i] - heappop(min_heap)
            right_sum[i] = total

        # Compare and get the minimum difference
        min_diff = float('inf')
        for i in range(n - 1, 2 * n):
            min_diff = min(min_diff, left_sum[i] - right_sum[i + 1])

        return min_diff