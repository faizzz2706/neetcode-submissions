
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        dummy = ListNode(-1)
        prev = dummy
        for i in range(1, len(lists)):
            prev = dummy
            prev.next = lists[0]
            curr = prev.next
            l2 = lists[i]
            while curr and l2:
                if curr.next and curr.val < l2.val and curr.next.val < l2.val:
                    prev = curr
                    curr = curr.next
                    continue
                
                if curr.val <= l2.val:
                    next1 = curr.next
                    next2 = l2.next
                    curr.next = l2
                    l2.next = next1
                    prev = l2
                    curr = next1
                    l2 = next2
                
                elif curr.val > l2.val:
                    next2 = l2.next
                    prev.next = l2
                    l2.next = curr
                    prev = l2
                    l2 = next2
            
            lists[0] = dummy.next
            if l2:
                prev.next = l2
        
        return dummy.next





