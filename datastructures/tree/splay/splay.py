class Node(object):

    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data is None:
            self.data = data
            self.splay()
        if data < self.data:
            if self.left is None:
                self.left = Node(data, self)
                self.left.splay()
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data, self)
                self.right.splay()
            else:
                self.right.insert(data)
        elif data == data:
            self.splay()

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
            data = self.data
            self.splay()
            return data

    def right_child_of(self):
        if self.parent.left is self:
            return False
        return True

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

    def zig_zig_left_left(self):
        p = self.parent
        g = p.parent
        p.rotate_left()
        g.rotate_left()

    def zig_zig_right_right(self):
        p = self.parent
        g = p.parent
        p.rotate_right()
        g.rotate_right()

    def zig_zag_left_right(self):
        p = self.parent
        g = p.parent
        p.rotate_left()
        g.rotate_right()

    def zig_zag_right_left(self):
        p = self.parent
        g = p.parent
        p.rotate_right()
        g.rotate_left()

    def splay(self):
        if self.parent is None:
            return
        if self.parent.parent is None:
            if self.right_child_of():
                self.parent.rotate_left()
            else:
                self.parent.rotate_right()
            return
        else:
            this_side = self.right_child_of()
            parent_side = self.parent.right_child_of()

            if this_side is False and parent_side is False:
                self.zig_zig_right_right()
            elif this_side is False and parent_side is True:
                self.zig_zag_right_left()
            elif this_side is True and parent_side is True:
                self.zig_zig_left_left()
            else:
                self.zig_zag_left_right()
            if self.parent.parent is not None:
                self.parent.parent.splay()
