from abstract_heap import AbstractHeap


class MaxHeap(AbstractHeap):

    def __init__(self):
        super().__init__()

    def __iter__(self):
        iterator = sorted(self.heap[1:], reverse=True)
        for x in iterator:
            yield x

    def _perc_up(self, index):
        parent = index // 2

        while parent > 0:
            if self.heap[index] > self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index //= 2
            parent = index // 2

    def _perc_down(self, index):
        while index * 2 <= self.size:
            temp = self.successor_child_index(index)
            if self.heap[index] < self.heap[temp]:
                self.heap[index], self.heap[temp] = self.heap[temp], self.heap[index]
            index = temp

    def successor_child_index(self, index):
        if index * 2 + 1 > self.size:
            return index * 2

        if self.heap[index*2] > self.heap[index*2+1]:
            return index * 2
        else:
            return index * 2 + 1
