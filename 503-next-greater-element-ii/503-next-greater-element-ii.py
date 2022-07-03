class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        res = [0 for _ in range(n)]
        stk = []
        
        for i in range(2 * n - 1, -1, -1):
            while stk and stk[-1] <= nums[i % n]:
                stk.pop()
            res[i % n] = -1 if not stk else stk[-1]
            stk.append(nums[i % n])
            
        return res
    
