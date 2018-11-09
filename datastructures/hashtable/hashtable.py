class LinkedList(object):
    """Linked list used as hash table indices for
       collision avoidance.
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
        """Node for linked list.
        """

        def __init__(self, key, value, next=None):
            self.key = key
            self.value = value
            self.next = next


class HashTable(object):
    """Hash table implementation which uses linked lists
       as list indices for collision avoidance.
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
        """Get an element from the table by key.
           O(1) best time O(n) worst time.

        args:
            key: Key to retrieve value pair of.

        return: Value of key argument if it exists in the table.
        """

        index = self._hash_function(key)

        if self.table[index] is not None:
            probe = self.table[index].head

            while probe is not None:
                if probe.key == key:
                    return probe.value
                probe = probe.next
        return None

    def delete(self, key):
        """Remove a key-value pair from the table by key.
           O(1) best time O(n) worst time.

        args:
            key: Key of key-value pair to remove from the table.
        """

        index = self._hash_function(key)

        if self.table[index] is not None:
            probe = self.table[index].head
            previous = probe

            if probe.key == key:
                if probe.next is None:
                    self.table[index] = None
                else:
                    self.table[index].head = self.table[index].head.next

            while probe is not None and probe.key != key:
                previous = probe
                probe = probe.next

            if probe is not None:
                previous.next = probe.next
                self.length -= 1

    def put(self, key, value):
        """Insert a key-value pair into the table. 
           O(1) best time O(n) worst time.

        args:
            key: Key to hash for generating list index.
            value: Value to store at index generated by key.
        """

        index = self._hash_function(key)

        if self.table[index] is None:
            self.table[index] = LinkedList()
            self.table[index].push(key, value)
        else:
            probe = self.table[index].head

            while probe is not None:
                if probe.key == key:
                    probe.value = value
                    return
                tail = probe
                probe = probe.next
            tail.next = LinkedList.Node(key, value)
        self.length += 1

    def _hash_function(self, key):
        """Determine the index position in the table to 
           store the key-value pair at.

        args:
            key: Key used to generate a hash for.
        """

        _hash = 0
        offset = 0  # Used so permutations generate different hashes.

        if isinstance(key, str):
            for x in key:
                _hash += ord(x) * offset
                offset += 1
        else:
            for x in str(int(key)):
                _hash += int(x) * offset
                offset += 1
        return _hash % self.size
