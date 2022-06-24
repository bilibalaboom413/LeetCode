class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        
        for i in range(len(s)):
            s1 = self.palindrome(s, i, i)
            s2 = self.palindrome(s, i, i + 1)
            # print(s1, s2, res)
            res = res if len(res) > len(s1) else s1
            res = res if len(res) > len(s2) else s2
            
            
        return res
    
    def palindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        
        # print(s[l:r])
        return s[l+1:r]
        