class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            if self.stack[-1][1] > val:
                self.stack.append((val,val))
            else:
                self.stack.append((val, self.stack[-1][1]))

    def pop(self) -> None:
        num = self.stack.pop()
        return num[0]
    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
