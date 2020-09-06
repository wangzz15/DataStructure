class DisjointSetNode:
    def __init__(self, x):
        self.val = x
        self.parent = self
        self.rank = 0

class DisjointSet:
    self.__init__(self, n):
        self.nodeList = []
        for i in range(n):
            self.nodeList.append(DisjointSetNode(i))

    def Union(self, x, y):
        if not self.inSameSet(x, y):
            self.Link(self.FindSet(self.nodeList[x]), self.FindSet(self.nodeList[y]))

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

    def inSameSet(self, x, y):
        return self.FindSet(self.nodeList[x]) == self.FindSet(self.nodeList[y])