class TrieNode:
    def __init__(self):
        self.child = [0] * 26
        self.isWord = False
        self.id = -1

class Trie:
    def __init__(self):
        self.nodeList = [TrieNode()]

    def insert(self, word: str, id) -> None:
        cursor = 0
        for char in word:
            index = ord(char) - ord('a')
            if self.nodeList[cursor].child[index] == 0:
                self.nodeList.append(TrieNode())
                self.nodeList[cursor].child[index] = len(self.nodeList) - 1
            cursor = self.nodeList[cursor].child[index]
        self.nodeList[cursor].isWord = True
        self.nodeList[cursor].id = id

    def search(self, word: str) -> bool:
        cursor = 0
        for char in word:
            index = ord(char) - ord('a')
            if self.nodeList[cursor].child[index] == 0:
                return False
            cursor = self.nodeList[cursor].child[index]
        return self.nodeList[cursor].isWord        

    def startsWith(self, prefix: str) -> bool:
        cursor = 0
        for char in prefix:
            index = ord(char) - ord('a')
            if self.nodeList[cursor].child[index] == 0:
                return False
            cursor = self.nodeList[cursor].child[index]
        return True

    def prefixOf(self, word):
        res = []
        cursor = 0
        for char in word:
            index = ord(char) - ord('a')
            cursor = self.nodeList[cursor].child[index]
            if self.nodeList[cursor].isWord:
                res.append(self.nodeList[cursor].id)
            if cursor == 0:
                return res            
        return res