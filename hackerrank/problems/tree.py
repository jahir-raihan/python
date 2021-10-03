class TreeNode:
    def __init__(self, name, deg):
        self.name = name
        self.deg = deg
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print(self, category='both'):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|__' if self.parent else ''
        if category == 'name':
            print(prefix + self.name)
        elif category == 'deg':
            print(prefix + self.deg)
        elif category == "both":
            print(prefix + self.name + f'-->({self.deg})')
        if self.children:
            for child in self.children:
                child.print(category)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level +=1
            p = p.parent
        return level


def build_product_tree():
    Nilpul = TreeNode('Nilpul', 'CEO')

    Chinmay = TreeNode('Chinmay','CTO')
    Vishaw = TreeNode('Vishaq', 'Infrastructure Head')
    Dhaval = TreeNode('Dhaval', 'Cloud Manager')
    Abhijit = TreeNode('Abhijit', 'App Manager')
    Amir = TreeNode('Amir', 'Application Head')
    Chinmay.add_child(Vishaw)
    Vishaw.add_child(Dhaval)
    Vishaw.add_child(Abhijit)
    Chinmay.add_child(Amir)
    Nilpul.add_child(Chinmay)

    Gels = TreeNode('Gels', 'HR Head')
    Gels.add_child(TreeNode('Peter', 'Recruitment Manager'))
    Gels.add_child(TreeNode('Waqas', 'Policy Manager'))
    Nilpul.add_child(Gels)

    return Nilpul


if __name__ == '__main__':
    root = build_product_tree()
    root.print('deg')

