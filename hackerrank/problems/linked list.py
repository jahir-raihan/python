class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beg(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print('linked list is empty')
            return
        itr = self.head
        while itr:
            print(itr.data, end=' ')
            itr = itr.next
        print('\n')

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_elements(self, values):
        self.head = None
        for data in values:
            self.insert_at_end(data)

    def get_level(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, pos):
        if pos < 0 or pos > self.get_level():
            raise Exception('invalid index')
        if pos == 0:
            self.head = self.head.next
        count = 0
        itr = self.head
        while itr:
            if count == pos - 1:
                itr.next = itr.next.next

            itr = itr.next
            count += 1

    def insert_at(self, pos, data):
        if pos == 0:
            self.insert_at_beg(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == pos - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def pop(self):
        count = 0
        itr = self.head
        while itr:
            if count == self.get_level() - 2:
                itr.next = None
                break
            itr = itr.next
            count += 1

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
            print(prev.data)
        self.head = prev


ll = LinkedList()
ll.insert_at_end(3)
ll.insert_at_end(5)
ll.insert_at_end(7)
ll.insert_at_end(8)
ll.insert_at_end(9)
ll.insert_at_end(2)
ll.remove_at(2)
ll.insert_at(2, 6)
ll.print()
ll.pop()

ll.print()
ll.reverse()
ll.print()
