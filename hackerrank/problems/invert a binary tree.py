
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
        if self.root is None:
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


tree = BinarySearchTree()
arr = [4, 2, 3, 1, 7, 6, 9]
for i in range(len(arr)):
    tree.create(arr[i])

queue = [tree.root,]
while queue:
    val = queue.pop(0)
    if val is None:
        continue
    val.left, val.right = val.right, val.left

    queue.append(val.right)
    queue.append(val.left)

# s = []
# cur = tree.root
# while True:
#     if cur:
#         s.insert(0, cur)
#         cur = cur.left
#     elif s:
#         val = s.pop(0)
#         print(val.info, end=' ')
#         cur = val.right
#     else:
#         break

s = []
cur = tree.root
res = []
while True:
    if cur:
        s.insert(0, cur)
        cur = cur.left
    elif s:
        val = s.pop(0)
        print(val.info, end=' ')
        res.append(val.info)
        cur = val.right
    else:
        break
