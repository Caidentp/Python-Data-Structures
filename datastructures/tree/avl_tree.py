class Node:
    
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None
        
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data, self)
                    self.left._self_balance()
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data, self)
                    self.right._self_balance()
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def _rotate_right(self):

        pivot = self.left

        if pivot is None:
            return

        temp = self.data
        self.data = pivot.data
        pivot.data = temp
        
        self.left = pivot.left

        if self.left is not None:
            self.left.parent = self

        pivot.left = pivot.right

        if pivot.left is not None:
            pivot.left.parent = pivot

        pivot.right = self.right

        if pivot.right is not None:
            pivot.right.parent = pivot

        self.right = pivot
        pivot.parent = self


    def _rotate_left(self):
        pivot = self.right

        if pivot is None:
            return

        temp = self.data
        self.data = pivot.data
        pivot.data = temp
        
        self.right = pivot.right

        if self.right is not None:
            self.right.parent = self

        pivot.right = pivot.left

        if pivot.right is not None:
            pivot.right.parent = pivot

        pivot.left = self.left

        if pivot.left is not None:
            pivot.left.parent = pivot

        self.left = pivot
        pivot.parent = self

            
    def _self_balance(self):
        balance = self.balance()

        if balance == 2:
            if self.left.balance() <= -1:
                self.left._rotate_left()

            self._rotate_right()

            if self.parent is not None:
                self.parent._self_balance()

        elif balance == -2:
            if self.right.balance() >= 1:
                
                self.right._rotate_right()

            self._rotate_left()

            if self.parent is not None:
                self.parent._self_balance()

        else:
            if self.parent is not None:
                self.parent._self_balance()
            
    def balance(self):
        if self.left is not None:
            left_depth = self.left.depth()
        else:
            left_depth = 0
        if self.right is not None:
            right_depth = self.right.depth()
        else:
            right_depth = 0
        return left_depth - right_depth
            
    def depth(self):
        if self.left is not None:
            left_depth = self.left.depth()
        else:
            left_depth = 0
        if self.right is not None:
            right_depth = self.right.depth()
        else:
            right_depth = 0
        return max(left_depth, right_depth) + 1
            
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data, end=" ")
        if self.right:
            self.right.inorder()
