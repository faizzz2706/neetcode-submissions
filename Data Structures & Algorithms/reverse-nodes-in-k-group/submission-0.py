# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head, tail):
        prev = None
        new_tail = head
        stop = tail.next
        while head and head != stop:
            nextNode = head.next
            head.next = prev
            prev = head
            head = nextNode
        
        return [prev, new_tail]


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        dummy = ListNode(-1)
        dummy.next = head
        curr = head
        start = dummy
        end = None
        length = 1
        while curr:
            if length%k != 0:
                length += 1
                curr = curr.next
            
            elif length % k == 0:
                nextNode = curr.next

                end = curr
                new_head, new_tail = self.reverse(start.next, end)

                start.next = new_head
                new_tail.next = nextNode

                start = new_tail
                curr = nextNode
                length += 1
        
        return dummy.next
                




















