class Solution(object):
    
    def __init__(self):
        self.nums = []
        self.diff = []
            
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        
        # if n <= 0: return []
        
        self.nums = [0 for _ in range(n)]
        
        self.diff = [0 for _ in range(n)]
        
        self.diff[0] = self.nums[0]
        for i in range(1, n):
            self.diff[i] = self.nums[i] - self.nums[i - 1]
        
        for booking in bookings:
            i = booking[0] - 1
            j = booking[1] - 1
            val = booking[2]
            self.increment(i, j, val)
        
        return self.result()
    
    def increment(self, i, j, val):
        self.diff[i] += val
        if (j + 1) < len(self.diff):
            self.diff[j + 1] -= val
            
            
    def result(self):
        res = [0 for _ in range(len(self.diff))]
        res[0] = self.diff[0]
        
        for i in range(1, len(self.diff)):
            res[i] = res[i - 1] + self.diff[i]
            
        return res