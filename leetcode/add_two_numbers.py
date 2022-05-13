class Node:
    def __init__(self, item):
        self.val = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        return self.head.val

    def add(self, val):
        if self.head is None:
            self.head = Node(val)
            self.head.next = None
        else:
            head = self.head
            while head.next is not None:
                head = head.next
            head.next = Node(val)


# linked_list = LinkedList()
# linked_list.add(1)
# linked_list.add(2)
# linked_list.add(3)
# linked_list.add(4)
# linked_list.add(5)
# itr = linked_list.head
#
# while itr:
#     print(itr.val)
#     itr = itr.next

node = Node(1)
head = node

for i in range(2, 5):
    temp = Node(i)
    head.next = temp
    head = head.next
print(head.val)

while node:
    print(node.val)
    node = node.next

