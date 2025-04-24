import unittest
from skip_list import Node
from skip_list import SkipList

class TestSkipList(unittest.TestCase):
    def test_skiplist_creation(self):
        skiplist = SkipList()
        self.assertEqual(skiplist.head.data, float("-inf"), "Head value is wrong")
    
    def test_skiplist_insert(self):
        skiplist = SkipList()
        skiplist._insert(14)
        self.assertEqual(skiplist.head.data, float("-inf"), "Head value is wrong")
        self.assertIsInstance(skiplist.head.next, Node)
        self.assertEqual(skiplist.head.next.data, 14, "Node value is wrong")
    
    def test_skiplist_insert_between(self):
        skiplist = SkipList()
        skiplist._insert(14)
        skiplist._insert(20)
        skiplist._insert(17)
        skiplist._insert(34)

        skiplist._insert(11)
        skiplist._insert(25)
        skiplist._insert(107)
        skiplist._insert(322)

        skiplist._insert(145)
        skiplist._insert(2000)
        skiplist._insert(1734)
        skiplist._insert(341)

        skiplist._insert(113)
        skiplist._insert(256)
        skiplist._insert(147)
        skiplist._insert(3252)


        self.assertEqual(skiplist.head.data, float("-inf"), "Head value is wrong")
        self.assertIsInstance(skiplist.head.next, Node)
        self.assertEqual(skiplist.head.level, skiplist.head.next.level, "Levels are wrong")

    def test_skiplist_search(self):
        skiplist = SkipList()
        skiplist._insert(14)
        skiplist._insert(20)
        skiplist._insert(17)
        skiplist._insert(34)

        skiplist._insert(11)
        skiplist._insert(25)
        skiplist._insert(107)
        skiplist._insert(322)

        node = Node(107)
        self.assertIs(skiplist._search(node), node, "Not found")

    def test_skiplist_deletion(self):
        skiplist = SkipList()
        skiplist._insert(14)
        skiplist._insert(20)
        skiplist._insert(17)
        skiplist._insert(34)

        skiplist._insert(11)
        skiplist._insert(25)
        skiplist._insert(107)
        skiplist._insert(322)

        node1 = Node(107)
        node2 = Node(39)
        self.assertEqual(skiplist._delete(node1), "Node removed successfully", "Error deleting")
        self.assertEqual(skiplist._delete(node2), "Node was not found", "Error deleting")
if __name__ == "__main__":
    unittest.main()