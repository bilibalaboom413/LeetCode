# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
        from collections import deque
        
        stk = deque()
        
        p = head
        
        while p:
            stk.append(p)
            p = p.next
            
        p = head
        
        while p:
            lastNode = stk.pop()
            nextNode = p.next
            if lastNode == nextNode or lastNode.next == nextNode:
                lastNode.next = None
                break
            p.next = lastNode
            lastNode.next = nextNode
            p = nextNode
            
        
        