class LinkedList(object):
    """Linked list used as hash table indices.
    """

    def __init__(self):
        self.head = None

    def __iter__(self):
        probe = self.head

        while probe is not None:
            yield probe.data
            probe = probe.next            

    def push(self, key, value):
        self.head = LinkedList.Node(key, value, self.head)


    class Node(object):
        """Node used in LinkedList.
        """

        def __init__(self, key, value, next=None):
            self.key = key
            self.value = value
            self.next = next


class HashTable(object):
    """Hash table class. Table is represented by array of
    LinkedList objects for collision avoidance.
    """

    def __init__(self, size=1024):
        self.size = size
        self.table = [None] * self.size 
        self.length = 0

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __len__(self):
        return self.length

    def get(self, key):
        index = self._hash_function(key)

        if self.table[index] is not None:
            probe = self.table[index].head

            while probe is not None:
                if probe.key == key:
                    return probe.value
                probe = probe.next
        return None

    def put(self, key, value):
        index = self._hash_function(key)

        if self.table[index] is None:
            self.table[index] = LinkedList()
            self.table[index].push(key, value)

        else:
            probe = self.table[index].head

            while probe.next is not None:
                if probe.key == key:
                    probe.value = value
                    return
                probe = probe.next
            probe.next = LinkedList.Node(key, value)
        self.length += 1

    def _hash_function(self, key):
        _hash = 0

        if isinstance(key, str):
            for x in key:
                _hash += ord(x)
        else:
            for x in str(int(key)):
                _hash += int(x)
        return _hash % self.size
