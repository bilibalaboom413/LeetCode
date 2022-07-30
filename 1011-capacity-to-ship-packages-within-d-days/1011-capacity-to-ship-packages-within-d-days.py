class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        
        while left < right:
            mid = left + (right - left) // 2
            if self.f(weights, mid) <= days:
                right = mid
            elif self.f(weights, mid) > days:
                left = mid + 1
        
        return left
    
    def f(self, weights, x):
        days = 0
        index = 0
        
        while index < len(weights):
            cap = x
            while index < len(weights):
                if cap < weights[index]:
                    break
                cap -= weights[index]
                index += 1
                
            days += 1
        
        return days
        