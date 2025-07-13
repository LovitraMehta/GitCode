import heapq

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        heapq.heapify(players)
        heapq.heapify(trainers)
        
        match_count = 0
        
        while players and trainers:
            if players[0] <= trainers[0]:
                heapq.heappop(players)
                heapq.heappop(trainers)
                match_count += 1
            else:
                heapq.heappop(trainers)
        
        return match_count