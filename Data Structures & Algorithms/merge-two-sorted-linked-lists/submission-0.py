# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2
        if not list2:
            return list1

        curr1 = list1
        curr2 = list2

        dummy = ListNode(0)
        dummy.next = list1
        prev = dummy

        while curr1 and curr2:

            if curr1.next and curr1.val <= curr2.val and curr1.next.val < curr2.val:
                prev = curr1
                curr1 = curr1.next

            elif curr1.val <= curr2.val:
                nextNode1 = curr1.next
                nextNode2 = curr2.next

                curr1.next = curr2
                curr2.next = nextNode1

                prev = curr2
                curr2 = nextNode2

            else:
                nextNode2 = curr2.next

                prev.next = curr2
                curr2.next = curr1

                prev = curr2
                curr2 = nextNode2

        if curr2:
            prev.next = curr2

        return dummy.next