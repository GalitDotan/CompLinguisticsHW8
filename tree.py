class Node:
    def __init__(self, key, children):
        self.key = key
        self.children = []

    def __repr__(self):
        if self.children:
            return '[{} {}]'.format(self.key, ' '.join(map(repr, self.children)))
        else:
            return self.key


class Tree:
    def __init__(self, root=None):
        self.root = root

    def __repr__(self):
        return '{}'.format(repr(self.root))
