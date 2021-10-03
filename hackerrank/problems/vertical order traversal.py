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


def vertical(root):
    q = Queue()
    root_val = {root.info: 0,}
    q.put(root)
    while not q.empty():
        c = q.get()
        if c.left:
            temp = c.left
            q.put(temp)
            root_val[temp.info] = root_val[c.info] - 1
        if c.right:
            temp = c.right
            q.put(temp)
            root_val[temp.info] = root_val[c.info] + 1
    return root_val


tree = BinarySearchTree()
arr = [ 'e', 'f', 'g', 'h', 'a', 'b', 'c', 'd']
for i in range(len(arr)):
    tree.create(arr[i])
res = {}
for k, v in vertical(tree.root).items():
    try:
        res[v].append(k)
    except:
        res[v] = [k]

print(res)


