class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        left, right = 1, 10**9 + 1
        # print(right)
        while left <= right:
            # speed 
            mid = (left + right) // 2
            
            if self.f(piles, mid) == h:
                right = mid - 1
            # too fast
            elif self.f(piles, mid) < h:
                right = mid - 1
            # too slow
            elif self.f(piles, mid) > h:
                left = mid + 1
        
        return left
        
    def f(self, piles, x):
        hours = 0
        
        for pile in piles:
            hours += pile // x
            
            if pile % x > 0:
                hours += 1
            
        return hours