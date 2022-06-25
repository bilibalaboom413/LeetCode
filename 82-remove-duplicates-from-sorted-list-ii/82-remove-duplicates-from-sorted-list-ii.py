# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        p, q = dummy, head
        
        while q:
            if q.next and q.val == q.next.val:
                while q.next and q.val == q.next.val:
                    q = q.next
                # p.next = q
                q = q.next
                if not q: # after duplicate nodes q is null
                    p.next = None
            else:
                p.next = q
                p = p.next
                q = q.next
        
        return dummy.next
                
                
        