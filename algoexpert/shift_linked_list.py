class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next





class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        if self.head is None:
            self.head = Node(data, self.head)
            return
        itr = self.head

        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)
        return

L = LinkedList()

for i in range(10):
    L.add(i)

l = L.head

while l:
    print(l.data)
    l = l.next