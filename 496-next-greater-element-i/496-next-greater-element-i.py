class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater = self.func(nums2)
        greaterMap = {}
        for i in range(len(nums2)):
            greaterMap[nums2[i]] = greater[i]
            
        res = [0 for _ in range(len(nums1))]
        
        for i in range(len(nums1)):
            res[i] = greaterMap[nums1[i]]
        
        return res
    
    def func(self, nums):
        n = len(nums)
        
        res = [0 for _ in range(n)]
        stk = []
        
        for i in range(n - 1, -1, -1):
            while stk and stk[-1] <= nums[i]:
                stk.pop()
            res[i] = -1 if not stk else stk[-1]
            stk.append(nums[i])
            
        return res