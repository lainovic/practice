import unittest

from src.hashmap import HashMap, KeyNotFoundError


class HashMapTest(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.map = HashMap()
        self.map.put(55, 422)
        self.map.put(0, "wat")
        self.map.put(143, "watwat")
        self.map.put(212, "watwat")
        self.map.put(67, "watwatwat")
        self.map.put(167, "edamame")
        self.map.put(7, "Hi")
        self.map.put(7, "foo")
        self.map.put(107, "bar")
        self.map.put(207, "baz")

    def test_get(self):
        self.assertEqual(self.map.get(67), "watwatwat")
        self.assertEqual(self.map.get(167), "edamame")
        self.assertEqual(self.map.get(7), "foo")
        self.assertEqual(self.map.get(107), "bar")
        self.assertEqual(self.map.get(207), "baz")

    def test_remove(self):
        self.map.remove(107)
        self.assertEqual(self.map.get(7), "foo")
        self.assertEqual(self.map.get(207), "baz")
        self.map.remove(7)
        self.assertEqual(self.map.get(207), "baz")
        self.map.remove(7)
        self.map.remove(207)
        with self.assertRaises(KeyNotFoundError):
            self.map.get(207)


if __name__ == "__main__":
    unittest.main()
