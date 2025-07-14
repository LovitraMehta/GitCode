class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        num = 0
        while head:
            # Shift the current value to the left and add the new bit
            num = (num << 1) | head.val
            head = head.next
        return num
