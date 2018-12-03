class Node:

    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if not self.left:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            if data > self.data:
                if not self.right:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def contains(self, value):
        if self.data == value:
            return True
        elif value < self.data:
            if not self.left:
                return False
            else:
                return self.left.contains(value)
        else:
            if not self.right:
                return False
            else:
                return self.left.contains(value)

    def delete_node(self, data):
        node, parent = self.lookup(data)
        if node:
            child_count = node.children_count()

            if child_count == 0:
                if parent:
                    if parent.left is node:
                        parent.left = None
                    elif parent.right is node:
                        parent.right = None
                    del node
                else:
                    self.data = None

            elif child_count == 1:
                if node.left:
                    n = node.left
                else:
                    n = node.right
                if parent:
                    if parent.left is node:
                        parent.left = n
                    else:
                        parent.right = n
                    del node
                else:
                    self.left = n.left
                    self.right = n.right
                    self.data = n.data

            else:
                parent = node
                successor = node.right

                while successor.left:
                    parent = successor
                    successor = successor.left
                node.data = successor.data
                if parent.left == successor:
                    parent.left = successor.right
                else:
                    parent.right = successor.right

    def pre_order(self):
        print(self.data, end=" ")
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()

    def in_order(self):
        if self.left:
            self.left.in_order()
        print(self.data, end=" ")
        if self.right:
            self.right.in_order()

    def post_order(self):
        if self.left:
            self.left.post_order()
        if self.right:
            self.right.post_order()
        print(self.data, end=" ")

    def children_count(self):
        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1
        return count

    def lookup(self, data, parent=None):
        if data < self.data:
            if not self.left:
                return None, None
            return self.left.lookup(data, self)
        elif data > self.data:
            if not self.right:
                return None, None
            return self.right.lookup(data, self)
        else:
            return self, parent
