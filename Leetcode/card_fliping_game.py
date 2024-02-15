class Solution(object):
    def flipgame(self, fronts, backs):
        forbidden = set(fronts[i] for i in range(len(fronts)) if fronts[i] == backs[i])
        min_good = float('inf')
        
        for num in fronts + backs:
            if num not in forbidden:
                min_good = min(min_good, num)
                
        return min_good if min_good != float('inf') else 0
