class TrieNode:
    def __init__(self):
        self.children = [None]*26 # There are 26 letters in a word
        self.isEnd = False    

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for i in word:
            index = ord(i)-ord('a')
            if curr.children[index] is None:
                #Creating a new node if it does not exist at that point
                curr.children[index] = TrieNode()                
            curr = curr.children[index]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.root
        for i in word:
            index = ord(i)-ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return curr.isEnd

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in prefix:
            index = ord(i)-ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return True
        
        