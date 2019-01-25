class Graph(object):
    def __init__(self):
        self.master_list = dict()

    def __repr__(self):
        return repr(self.master_list)

    def __str__(self):
        return str(self.master_list.__str__)

    def __len__(self):
        return len(self.master_list)

    def __contains__(self, vertex):
        return vertex in self.master_list

    def __getitem__(self, key):
        return self.master_list[key]

    def __setitem__(self, key, new):
        self.master_list[key] = new

    def add_vertex(self, key):
        if key not in self:
            self[key] = dict()

    def get_vertex(self, key):
        if key in self:
            return self[key]

    def add_edge(self, v1, v2, weight=0):
        if v1 not in self:
            self.add_vertex(v1)
        if v2 not in self:
            self.add_vertex(v2)
        self[v1].update({v2: weight})

    def neighbors(self, vertex):
        return self[vertex]

    def adjacent(self, v1, v2):
        return v2 in self[v1]
