class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        current = self.root
        for i in word:
            index = ord(i)-ord('a')
            if current.children[index] is None:
                current.children[index] = TrieNode()
            current = current.children[index]
        current.isEnd = True


    def search(self, word: str) -> bool:
        current = self.root
        for i in word:
            index = ord(i)-ord('a')
            if current.children[index] is None:
                return False
            current = current.children[index]
        return current.isEnd

        

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for i in prefix:
            index = ord(i)-ord('a')
            if current.children[index] is None:
                return False
            current = current.children[index]
        return True

        
        