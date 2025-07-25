class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        lastNonZeroFoundAt = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[lastNonZeroFoundAt] = nums[lastNonZeroFoundAt], nums[i]
                lastNonZeroFoundAt += 1