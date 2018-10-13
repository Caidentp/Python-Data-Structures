class Heap:
    
    def __init__(self):
        self.heap = [0]
        self.size = 0
        
    def __repr__(self):
        template = "{}({})"
        return template.format(self.__class__.__name__, self.__dict__)
    
    def __str__(self):
        template = "<{} object at {}>"
        mem_address = '0x' + '{:0>16}'.format(hex(id(self)).upper()[2:])
        return template.format(self.__class__.__name__, mem_address)
        
    def __add__(self, other):
        new_heap = Heap()
        for item in self.heap:
            new_heap.insert(item)
        for item in other.heap:
            new_heap.insert(item)
        return new_heap
    
    def __iter__(self):
        iterator = sorted(self.heap[1:])
        for x in iterator:
            yield x

    def __len__(self):
        return self.size
        
    def insert(self, data):
        self.heap.append(data)
        self.size += 1
        self._perc_up(self.size)
        
    def _perc_up(self, index):
        parent = index // 2
        while parent > 0:
            if self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index //= 2
            parent = index // 2
            
    def _perc_down(self, index):
        while index * 2 <= self.size:
            temp = self.min_child_index(index)
            if self.heap[index] > self.heap[temp]:
                self.heap[index], self.heap[temp] = self.heap[temp], self.heap[index]
            index = temp
            
    def min_child_index(self, index):
        if index * 2 + 1 > self.size:
            return index * 2
        if self.heap[index*2] < self.heap[index*2+1]:
            return index * 2
        else:
            return index * 2 + 1
        
    def delete_min(self):
        minimum = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self._perc_down(1)
        return minimum
    
    @classmethod
    def from_iterable(cls, iterable):
        new_heap = cls()
        new_heap.size = len(iterable)
        new_heap.heap += list(iterable)
        x = len(iterable) // 2
        while x > 0:
            new_heap._perc_down(x)
            x -= 1
        return new_heap
