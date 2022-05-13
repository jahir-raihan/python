"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def __init__(self):
        self.dic = {}

    def traverse(self, root, level):
        if root:
            if level in self.dic:
                self.dic[level].append(root)
            else:
                self.dic[level] = [root]
            level += 1
            self.traverse(root.left, level)
            self.traverse(root.right, level)

        return

    def connect(self, root):
        self.traverse(root, 0)
        temp = [val for _, val in self.dic.items()]

        for _ in range(len(temp)):
            element = temp.pop(0)
            val = element.pop(0)

            for _ in range(len(element)):
                val.next = element[0]
                val = element.pop(0)
        return root
