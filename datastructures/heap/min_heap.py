from abstract_heap import AbstractHeap


class MinHeap(AbstractHeap):
    def __init__(self):
        super().__init__()

    def __iter__(self):
        iterator = sorted(self[1:])
        for x in iterator:
            yield x

    def _perc_up(self, index):
        parent = index // 2

        while parent > 0:
            if self[index] < self[parent]:
                self[index], self[parent] = self[parent], self[index]
            index //= 2
            parent = index // 2

    def _perc_down(self, index):
        while index * 2 <= self.size:
            temp = self.successor_child_index(index)
            if self[index] > self[temp]:
                self[index], self[temp] = self[temp], self[index]
            index = temp

    def successor_child_index(self, index):
        if index * 2 + 1 > self.size:
            return index * 2

        if self[index*2] < self[index*2+1]:
            return index * 2
        return index * 2 + 1
