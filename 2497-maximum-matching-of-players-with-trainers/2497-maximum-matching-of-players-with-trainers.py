class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        
        i, j = 0, 0  # i for players, j for trainers
        match_count = 0
        
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                match_count += 1
                i += 1
                j += 1
            else:
                j += 1  # Trainer can't match player[i], try next trainer
                
        return match_count