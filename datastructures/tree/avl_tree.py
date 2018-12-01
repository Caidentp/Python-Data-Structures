class Node(object):

    def __init__(self, data=None, parent=None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data is not None:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data, self)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data, self)
                else:
                    self.right.insert(data)
            self.self_balance()
        else:
            self.data = data

    def find(self, data):
        if data < self.data:
            if self.left is not None:
                return self.left.find(data)
            else:
                return None
        elif data > self.data:
            if self.right is not None:
                return self.right.find(data)
            else:
                return None
        else:
            return self

    def delete(self, data):
        node = self.find(data)
        if node is not None:
            child_count = node.children()
            parent = node.parent

            if child_count == 0:
                if parent is not None:
                    if parent.left is node:
                        parent.left = None
                    else:
                        parent.right = None
                else:
                    self.data = None

            elif child_count == 1:
                if node.left is not None:
                    successor = node.left
                else:
                    successor = node.right
                if parent is not None:
                    if parent.left is node:
                        parent.left = successor
                    else:
                        parent.right = successor
                else:
                    self.left = successor.left
                    self.right = successor.right
                    self.data = successor.data

            else:
                parent = node
                successor = parent.right

                while successor.left is not None:
                    parent = successor
                    successor = successor.left
                node.data = successor.data

                if parent.left is successor:
                    parent.left = successor.right
                else:
                    parent.right = successor.right

            node.self_balance()

    def depth(self):
        left_depth = 0 if self.left is None else self.left.depth()
        right_depth = 0 if self.right is None else self.right.depth()
        return 1 + max(left_depth, right_depth)

    def balance(self):
        left_depth = 0 if self.left is None else self.left.depth()
        right_depth = 0 if self.right is None else self.right.depth()
        return left_depth - right_depth

    def rotate_right(self):
        if self.left is None:
            return

        successor = self.left
        self.data, successor.data = successor.data, self.data
        self.left = successor.left

        if self.left is not None:
            self.left.parent = self

        successor.left = successor.right
        successor.right = self.right

        if successor.right is not None:
            successor.right.parent = successor
        self.right = successor

    def rotate_left(self):
        if self.right is None:
            return

        successor = self.right
        self.data, successor.data = successor.data, self.data
        self.right = successor.right

        if self.right is not None:
            self.right.parent = self

        successor.right = successor.left
        successor.left = self.left

        if successor.left is not None:
            successor.left.parent = successor
        self.left = successor

    def self_balance(self, flag=False):
        balance = self.balance()

        if balance == 2:
            if self.left.balance() <= -1:
                self.left.rotate_left()
            self.rotate_right()

            if self.parent is not None:
                self.parent.self_balance()

        elif balance == -2:
            if self.right.balance() >= -1:
                self.right.rotate_right()
            self.rotate_left()

            if self.parent is not None:
                self.parent.self_balance()

        else:
            if self.parent is not None:
                self.parent.self_balance()

    def children(self):
        count = 0
        if self.left is not None:
            count += 1
        if self.right is not None:
            count += 1
        return count
