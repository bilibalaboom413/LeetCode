class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        
        need = {}
        window = {}
        
        for i in t:
            if i in need:
                need[i] += 1
            else:
                need[i] = 1
        
        left, right, valid = 0, 0, 0
        
        start, length = 0, float('inf')
        
        while right < len(s):
            c = s[right]
            right += 1
            
            if c in need:
                if c in window:
                    window[c] += 1
                else:
                    window[c] = 1
                
                if window[c] == need[c]:
                    valid += 1
            
            while valid == len(need):
                if right - left < length:
                    start = left
                    length = right - left
                
                d = s[left]
                left += 1
                
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        
        # print(start, length)
        
        return "" if length == float('inf') else s[start:start + length]