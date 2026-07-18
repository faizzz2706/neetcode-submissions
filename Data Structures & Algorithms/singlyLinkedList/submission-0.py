class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
class LinkedList:
    def __init__(self):
        self.dummy = ListNode(-1)
        self.dummy.next = None

    def get(self, index: int) -> int:
        i = 0
        curr = self.dummy.next
        while curr:
            if index == i:
                return curr.val
            else:
                i += 1
                curr = curr.next
        return -1
        

    def insertHead(self, val: int) -> None:
        temp = self.dummy.next
        new = ListNode(val)
        self.dummy.next = new
        new.next = temp

    def insertTail(self, val: int) -> None:
        if self.dummy.next == None:
            self.dummy.next = ListNode(val)
            return
        prev = None
        curr = self.dummy.next
        while curr:
            prev = curr
            curr = curr.next
        
        prev.next = ListNode(val)
    def remove(self, index: int) -> bool:
        if index == 0:
            if self.dummy.next:
                self.dummy.next = self.dummy.next.next
                return True
            else:
                return False
        
        i = 0
        curr = self.dummy.next
        prev = None
        while curr:
            if index == i:
                prev.next = prev.next.next
                return True
            else:
                prev = curr
                i += 1
                curr = curr.next
        return False
            
    def getValues(self) -> List[int]:
        res = []

        curr = self.dummy.next
        while curr:
            res.append(curr.val)
            curr = curr.next
        
        return res
        
