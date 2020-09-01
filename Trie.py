class TrieNode:
    def __init__(self, isLeaf=False, char="", depth=0):
        self.isLeaf = isLeaf 
        self.char = char
        self.depth = depth
        self.child = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, s):
	TrieNode()
