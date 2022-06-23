# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # Deal with null head
        dummy = ListNode(-1)
        dummy.next = head
        
        tmp = self.findFromEnd(dummy, n + 1)
        tmp.next = tmp.next.next
        
        return dummy.next
        
        
    
    def findFromEnd(self, head, k):
        p1, p2 = head, head
        for i in range(k):
            p2 = p2.next
        
        while p2:
            p1 = p1.next
            p2 = p2.next
        
        return p1