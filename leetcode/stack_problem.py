class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        return -1

    def doaddition(self, k, v):
        self.stack = [self.stack[x] + v for x in range(k)] + [self.stack[x] for x in range(k, len(self.stack))]

    def increment(self, k: int, val: int) -> None:
        if k >= len(self.stack):
            self.doaddition(len(self.stack), val)
        else:
            self.doaddition(k, val)

# Your CustomStack object will be instantiated and called as such:
obj = CustomStack(3)
obj.push(1)
obj.push(2)
print(obj.pop())
obj.push(2)
obj.push(3)
obj.push(4)
obj.increment(5,100)
obj.increment(2,100)
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())


# ["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
# [[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]