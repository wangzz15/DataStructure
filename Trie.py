class TrieNode:
    def __init__(self):
        self.child = [0] * 26
        self.isWord = False

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nodeList = [TrieNode()]
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cursor = 0
        for char in word:
            index = ord(char) - ord('a')
            if self.nodeList[cursor].child[index] == 0:
                self.nodeList.append(TrieNode())
                self.nodeList[cursor].child[index] = len(self.nodeList) - 1
            cursor = self.nodeList[cursor].child[index]
        self.nodeList[cursor].isWord = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cursor = 0
        for char in word:
            index = ord(char) - ord('a')
            if self.nodeList[cursor].child[index] == 0:
                return False
            cursor = self.nodeList[cursor].child[index]
        return self.nodeList[cursor].isWord        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cursor = 0
        for char in prefix:
            index = ord(char) - ord('a')
            if self.nodeList[cursor].child[index] == 0:
                return False
            cursor = self.nodeList[cursor].child[index]
        return True