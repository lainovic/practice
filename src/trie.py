class Trie:
    class Node:
        def __init__(self) -> None:
            self.is_end = False
            self.children = {}

    def __init__(self) -> None:
        self.root = self.Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = self.Node()
            curr = curr.children[letter]
        curr.is_end = True

    def remove(self, word) -> None:
        curr = self.root
        parents = []
        for letter in word:
            parents.append((letter, curr))
            curr = curr.children[letter]
        curr.is_end = False
        for key, parent in reversed(parents):
            if len(parent.children[key].children) > 0:
                break
            del parent.children[key]

    def search(self, word: str) -> bool:
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for letter in prefix:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]
        return True
