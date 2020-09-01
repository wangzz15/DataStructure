class DisjointSetNode:
    def __init__(self, x):
        self.val = x
        self.parent = self
        self.rank = 0

class DisjointSet:
    def MakeSet(self, val):
        return DisjointSetNode(val)
    def Union(self, x, y):
        self.Link(self.FindSet(x),self.FindSet(y))
    def Link(self, x, y):
        if x.rank > y.rank:
            y.parent = x
        else:
            x.parent = y
            if x.rank == y.rank:
                y.rank += 1
    def FindSet(self, x):
        if x != x.parent:
            x.parent = self.FindSet(x.parent)
        return x.parent

A = DisjointSet()
A = A.MakeSet(1)
print(A.parent==A)