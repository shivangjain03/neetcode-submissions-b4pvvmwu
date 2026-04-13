class TrieNode():
    def __init__(self):
        self.children = [None]*26
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()        

    def addWord(self, word: str) -> None:
        curr = self.root
        for i in word:
            index = ord(i)-ord('a')
            if curr.children[index] is None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.root
        def dfs(root, index):
            curr = root
            if curr is None:
                return False
            
            if index == len(word):
                return curr.isEnd
            
            if word[index] == ".":
                for i in range(26):
                    if curr.children[i] is not None:
                        if dfs(curr.children[i], index + 1): return True
                return False
            else:
                idx = ord(word[index])-ord('a')
                if curr.children[idx] is not None:
                    return dfs(curr.children[idx], index + 1)
                else:
                    return False
        return dfs(curr,0)