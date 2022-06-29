class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        need, window = {}, {}
        
        left, right, valid = 0, 0, 0
        
        for i in s1:
            if i in need:
                need[i] +=1
            else:
                need[i] = 1
        
        while right < len(s2):
            c = s2[right]
            right += 1
            
            if c in need:
                if c in window:
                    window[c] += 1
                else:
                    window[c] = 1
                if window[c] == need[c]:
                    valid += 1
            
            while right - left >= len(s1):
                if valid == len(need):
                    return True
                
                d = s2[left]
                left += 1
                
                if d in need:
                    # print(window[d])
                    # print(need[d])
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        
        return False
                    
                
            
        
        
        