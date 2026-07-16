class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.mydict = {}
        self.capacity = capacity

        self.head = ListNode(-1,-1)
        self.tail = ListNode(-1,-1)

        self.head.next = self.tail
        self.head.prev = None

        self.tail.next = None
        self.tail.prev = self.head

    def get(self, key: int) -> int:

        if key in self.mydict:
            node = self.mydict[key]
            self.moveToFront(node)
            return node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.mydict:
            node = self.mydict[key]
            node.val = value
            self.moveToFront(node)
        else:
            if len(self.mydict) == self.capacity:
                node = self.head.next
                self.removeNode(self.head.next)
                del self.mydict[node.key]
                self.mydict[key] = ListNode(key,value)
                self.addNode(self.mydict[key])
            else:
                self.mydict[key] = ListNode(key,value)
                self.addNode(self.mydict[key])
    def moveToFront(self, node):
        previous = node.prev
        upfront = node.next

        previous.next = upfront
        upfront.prev = previous

        beforeTail = self.tail.prev

        beforeTail.next = node
        node.next = self.tail
        node.prev = beforeTail
        self.tail.prev = node
    
    def removeNode(self,node):
        previous = node.prev
        upcoming = node.next

        previous.next = upcoming
        upcoming.prev = previous
    
    def addNode(self,node):
        previous = self.tail.prev

        previous.next = node
        node.next = self.tail
        node.prev = previous

        self.tail.prev = node

        
