import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()  # Sort by start time
        available = list(range(n))
        heapq.heapify(available)
        busy = []  # (end_time, room)
        room_count = [0] * n

        for start, end in meetings:
            # Free up rooms
            while busy and busy[0][0] <= start:
                free_time, room = heapq.heappop(busy)
                heapq.heappush(available, room)

            if available:
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))
            else:
                # Delay meeting until earliest end time
                free_time, room = heapq.heappop(busy)
                duration = end - start
                heapq.heappush(busy, (free_time + duration, room))

            room_count[room] += 1

        # Return room with max meetings, tie-breaker by smallest room number
        return min([i for i, count in enumerate(room_count) if count == max(room_count)])