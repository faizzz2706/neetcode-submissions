class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next

        dumm = ListNode(0)
        dumm.next = head

        curr = dumm
        for _ in range(length - n):
            curr = curr.next

        curr.next = curr.next.next

        return dumm.next