from collections import deque
from typing import List

class Solution:
    def maxFreeTime(
        self,
        eventTime: int,
        k: int,
        startTime: List[int],
        endTime: List[int],
    ) -> int:

        n = len(startTime)
        dq: deque[tuple[int, int]] = deque()    # (index, A_value) with A non‑decreasing
        best = 0

        pref = 0                                # Σ durations up to *before* j
        for j in range(n + 1):                  # j == n is the sentinel “right anchor after last meeting”
            # ---------------- maintain window ---------------------------------
            # window of allowed i is [j‑k‑1 , j‑1]  ➜ i_idx == i  (we store real i)
            while dq and dq[0][0] < j - k - 1:  # drop indices that slid out
                dq.popleft()

            # ---------------- use current window ------------------------------
            # right anchor value B[j]
            if j < n:
                B = startTime[j] - pref
            else:                               # sentinel
                B = eventTime - pref

            # minimal A in window = dq[0][1]
            if dq:                              # when j == 0, deque is empty → no left anchor yet
                gap = B - dq[0][1]
                if gap > best:
                    best = gap

            # ---------------- push new left anchor (meeting j) ----------------
            if j < n:                           # sentinel has no “A”
                duration = endTime[j] - startTime[j]
                pref_next = pref + duration
                A_j = endTime[j] - pref_next    # A value for meeting j

                while dq and dq[-1][1] >= A_j:  # keep deque monotone
                    dq.pop()
                dq.append((j, A_j))

                pref = pref_next                # advance prefix‑sum for next round

        return best
