# TC: O(n)
# SC: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(None, head)
        
        p1 = dummy
        p2 = dummy
        
        count = 0
        while count < n:
            p2 = p2.next
            count += 1
        
        while p2.next != None:
            p2 = p2.next
            p1 = p1.next
        
        p1.next = p1.next.next
        
        return dummy.next
        
        
        