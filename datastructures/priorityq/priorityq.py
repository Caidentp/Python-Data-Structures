class PriorityQ(object):
    def __init__(self):
        self.queue = [0]

    def __len__(self):
        return len(self.queue) - 1

    def __getitem__(self, index):
        return self.queue[index]

    def __setitem__(self, index, key):
        self.queue[index] = key

    def insert(self, data, priority=0):
        index = (data, priority)
        self.queue.append(index)
        self.percolate_up()

    def top(self):
        if not self.empty():
            return self[1][0]

    def del_top(self):
        if not self.empty():
            self[1], self[len(self)] = self[len(self)], self[1]
            data = self.queue.pop()[0]
            self.percolate_down()
            return data

    def percolate_up(self):
        child = len(self)
        parent = len(self) >> 1
        while parent > 0:
            if self[child][1] > self[parent][1]:
                self[child], self[parent] = self[parent], self[child]
            child = parent
            parent >>= 1

    def percolate_down(self):
        current = 1
        successor = self.max_child(current)
        while successor < len(self)+1:
            if self[current][1] < self[successor][1]:
                self[current], self[successor] = self[successor], self[current]
            current = successor
            successor = self.max_child(current)

    def max_child(self, index):
        if index*2+1 > len(self) or self[index*2][1] > self[index*2+1][1]:
            return index*2
        return index*2+1

    def empty(self):
        return len(self) == 0
