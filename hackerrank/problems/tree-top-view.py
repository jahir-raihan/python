from queue import Queue


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def topView(root):
    lis = [(root, 0)]
    res = {}
    while lis:
        node, point = lis.pop(0)
        if not node:
            continue
        if point not in res:
            res[point] = node.info
        lis.extend(
            [(node.left, point-1), (node.right, point+1)]
        )
    for _, val in sorted(res.items()):
        print(val, end=' ')


tree = BinarySearchTree()
arr = ['e', 'f', 'g', 'h', 'a', 'b', 'c', 'd']
for i in range(len(arr)):
    tree.create(arr[i])


topView(tree.root)


