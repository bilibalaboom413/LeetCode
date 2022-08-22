class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        
        return n - self.intervalSchedule(intervals)
    
    def intervalSchedule(self, intvs):
        if len(intvs) == 0: return 0
        
        intvs.sort(key = lambda x : x[1])
        
        count = 1
        x_end = intvs[0][1]
        
        for interval in intvs:
            if interval[0] >= x_end:
                count += 1
                x_end = interval[1]
                    
        return count
                
        
        