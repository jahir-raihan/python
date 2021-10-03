class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)

        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order(self):
        elements = []
        if self.left:
            elements += self.left.in_order()
        elements.append(self.data)

        if self.right:
            elements += self.right.in_order()

        return elements

    def search(self, val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            return False

    def find_min(self):
        if self.left is None:
            return self.data

        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def pre_order(self):
        elements = [self.data]

        if self.left:
            elements += self.left.pre_order()
        if self.right:
            elements += self.right.pre_order()
        return elements

    def post_order(self):
        elements = []
        if self.left:
            elements += self.left.post_order()
        if self.right:
            elements += self.right.post_order()
        elements.append(self.data)
        return elements

    def calculate_sum(self):
        left = self.left.calculate_sum() if self.left else 0
        right = self.right.calculate_sum() if self.right else 0
        return self.data + left + right

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)

        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.right

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)
        return self

    def get_level_by_value(self, val, count=1):
        if self.data == val:
            return count
        if val < self.data:
            if self.left:
                count += 1
                return self.left.get_level_by_value(val, count)
            return False
        if val > self.data:
            if self.right:
                count += 1
                return self.right.get_level_by_value(val, count)
            return False

    def left_level(self, left=0):
        if self.left is None:
            return left
        if self.left:
            left += 1
            return self.left.left_level(left)

    def right_level(self, right=0):
        if self.right is None:
            return right
        if self.right:
            right += 1
            return self.right.right_level(right)

    def find_max_level(self):
        left = self.left_level()
        right = self.right_level()
        if left > right:
            return left
        return right


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


numbers = [3, 5, 2, 1, 4, 6, 7]
nums_tree = build_tree(numbers)
print(nums_tree.right_level())
print(nums_tree.in_order())
