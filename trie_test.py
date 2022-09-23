from copy import deepcopy
import unittest

from trie import Trie


class TrieTest(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)

    def test_trie_search(self):
        trie = Trie()
        trie.insert("foo")
        self.assertTrue(trie.search("foo"))
        self.assertFalse(trie.search("fo"))
        self.assertTrue(trie.startsWith("fo"))

    def test_trie_remove(self):
        trie = Trie()
        trie.insert("bar")
        self.assertTrue(trie.search("bar"))
        trie.remove("bar")
        self.assertFalse(trie.search("bar"))
        trie.insert("bar")
        trie.insert("baz")
        self.assertTrue(trie.search("bar"))
        trie.remove("bar")
        self.assertFalse(trie.search("bar"))
        self.assertTrue(trie.startsWith("ba"))
        self.assertTrue(trie.search("baz"))


if __name__ == "__main__":
    unittest.main()
