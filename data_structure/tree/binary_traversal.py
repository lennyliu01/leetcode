import unittest
class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node({self.value})"

    def __str__(self):
        return f"Node({self.value})"


class BinaryTree:
    def __init__(self, root):
        self.root = root

    def __repr__(self):
        return f"BinaryTree({self.root})"

    def __str__(self):
        return f"BinaryTree({self.root})"

    def pre_order(self):
        """
        Pre-order traversal:
        1. Visit the root
        2. Traverse the left subtree
        3. Traverse the right subtree
        """
        output = []

        def _walk(node):
            if node is None:
                return
            output.append(node.value)
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)

        _walk(self.root)
        return output

    def in_order(self):
        """
        In-order traversal:
        1. Traverse the left subtree
        2. Visit the root
        3. Traverse the right subtree
        """
        output = []

        def _walk(node):
            if node is None:
                return
            if node.left:
                _walk(node.left)
            output.append(node.value)
            if node.right:
                _walk(node.right)

        _walk(self.root)
        return output

    def post_order(self):
        """
        Post-order traversal:
        1. Traverse the left subtree
        2. Traverse the right subtree
        3. Visit the root
        """
        output = []

        def _walk(node):
            if node is None:
                return
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)
            output.append(node.value)

        _walk(self.root)
        return output
class TestBinaryTree(unittest.TestCase):
    def test_pre_order(self):
        """
        Test pre-order traversal
        """
        tree = BinaryTree(Node(1))
        tree.root.left = Node(2)
        tree.root.right = Node(3)
        tree.root.left.left = Node(4)
        tree.root.left.right = Node(5)
        self.assertEqual(tree.pre_order(), [1, 2, 4, 5, 3])
    def test_in_order(self):
        """
        Test in-order traversal
        """
        tree = BinaryTree(Node(1))
        tree.root.left = Node(2)
        tree.root.right = Node(3)
        tree.root.left.left = Node(4)
        tree.root.left.right = Node(5)
        self.assertEqual(tree.in_order(), [4, 2, 5, 1, 3])
    def test_post_order(self):
        """
        Test post-order traversal
        """
        tree = BinaryTree(Node(1))
        tree.root.left = Node(2)
        tree.root.right = Node(3)
        tree.root.left.left = Node(4)
        tree.root.left.right = Node(5)
        self.assertEqual(tree.post_order(), [4, 5, 2, 3, 1])
    def test_empty_tree(self):
        """
        Test empty tree
        """
        tree = BinaryTree(None)
        self.assertEqual(tree.pre_order(), [])
        self.assertEqual(tree.in_order(), [])
        self.assertEqual(tree.post_order(), [])
if __name__ == "__main__":
    unittest.main() # run all tests