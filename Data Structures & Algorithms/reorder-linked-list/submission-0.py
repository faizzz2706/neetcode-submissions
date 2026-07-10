# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        head2 = slow.next
        slow.next = None
        

        prev = None
        while head2:
            nextNode = head2.next
            head2.next = prev
            prev = head2
            head2 = nextNode
        
        curr = head

        while curr and prev:

            nextNode1 = curr.next
            nextNode2 = prev.next

            curr.next = prev
            prev.next = nextNode1

            curr = nextNode1
            prev = nextNode2
        
        














