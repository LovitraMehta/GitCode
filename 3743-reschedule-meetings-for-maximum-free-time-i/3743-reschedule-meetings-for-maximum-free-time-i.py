from collections import deque
from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int,
                    k: int,
                    startTime: List[int],
                    endTime:   List[int]) -> int:

        n = len(startTime)

        # 1. durations & prefix sums
        P = [0]*(n+1)                         # P[t] = sum d[0:t]
        for i in range(n):
            P[i+1] = P[i] + (endTime[i] - startTime[i])

        slack = eventTime - P[n]              # total idle time already present

        # 2. build A (size n+1 with sentinel at index 0)
        A = [0]*(n+1)                         # A_idx = i+1  (so A[0] is sentinel for i = -1)
        for i in range(n):
            A[i+1] = endTime[i] - P[i+1]

        # 3. build B (size n+1 with sentinel at j = n)
        B = [0]*(n+1)
        for j in range(n):
            B[j] = startTime[j] - P[j]
        B[n] = slack

        # 4. sliding‑window minimum over A
        dq = deque()                          # stores indices in A
        ans = 0

        for j in range(n+1):                  # j = 0 … n
            # window is i ∈ [j-k-1 , j-1]  →  i_idx ∈ [j-k , j] (because i_idx = i+1)

            # drop indices left of window
            while dq and dq[0] < j - k:
                dq.popleft()

            # i = j-1  →  i_idx = j
            while dq and A[dq[-1]] >= A[j]:
                dq.pop()
            dq.append(j)

            # current minimum A in window
            minA = A[dq[0]]

            # calculate candidate gap
            gap = B[j] - minA
            if gap > ans:
                ans = gap

        return ans