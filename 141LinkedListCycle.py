# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head==None or head.next==None:
            return False
        slow=fast=head
        while fast and fast.next
            fast=head.next.next
            slow=head.next
            if fast=slow
                return True
        return False
            
        
