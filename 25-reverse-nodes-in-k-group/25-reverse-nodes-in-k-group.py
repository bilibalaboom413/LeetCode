# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head: return head
        a, b = head, head
        
        for i in range(k):
            if not b: return head
            b = b.next
        
        newHead = self.reverse(a, b)
        a.next = self.reverseKGroup(b, k)
        return newHead
        
    
    def reverse(self, head, tail):
        if not head or not head.next: 
            return head
        
        pre, cur, nxt = None, head, head
        
        while cur != tail:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        
        return pre