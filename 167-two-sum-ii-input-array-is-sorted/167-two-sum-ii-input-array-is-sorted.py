class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not numbers: return None
        
        lo, hi = 0, len(numbers) - 1
        while lo < hi:
            temp = numbers[lo] + numbers[hi]
            if temp == target:
                return [lo + 1, hi + 1]
            elif temp < target:
                lo += 1
            else:
                hi -= 1
        return [-1, -1]
                
        
        