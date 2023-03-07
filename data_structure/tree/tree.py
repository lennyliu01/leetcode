class TreeNode:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def build_tree(data_list):
    nodes = []
    for data in data_list:
        node = TreeNode(data[0], data[1])
        nodes.append(node)

    for i, node in enumerate(nodes):
        if node.parent is None:
            continue
        parent_index = [n.data for n in nodes].index(node.parent)
        parent = nodes[parent_index]
        parent.add_child(node)
        node.parent = parent

    return nodes[0] if nodes else None

# 生成一个简单的树
data_list = [(1, None), (2, 1), (3, 1), (4, 2), (5, 2), (6, 3), (7, 3)]
nodes = build_tree(data_list)

# 打印树
def print_tree(node, level=0):
    if node is not None:
        print("    " * level + str(node.data))
        for child in node.children:
            print_tree(child, level + 1)

print_tree(nodes)

# 生成一个简单的树
data_list = [(1, None), (2, 1), (3, 1), (4, 2), (5, 2), (6, 3), (7, 3)]
nodes = build_tree(data_list)



import unittest

class TestTreeNode(unittest.TestCase):
    def test_tree_node(self):
        node = TreeNode(1)
        self.assertEqual(node.data, 1)
        self.assertIsNone(node.parent)
        self.assertEqual(len(node.children), 0)

    def test_add_child(self):
        node1 = TreeNode(1)
        node2 = TreeNode(2)
        node1.add_child(node2)
        self.assertEqual(len(node1.children), 1)
        self.assertEqual(node1.children[0], node2)

class TestBuildTree(unittest.TestCase):
    def test_build_tree(self):
        data_list = [
            [1, None],
            [2, 1],
            [3, 1],
            [4, 2],
            [5, 2],
            [6, 3],
            [7, 3]
        ]
        root = build_tree(data_list)
        self.assertEqual(root.data, 1)
        self.assertEqual(len(root.children), 2)
        self.assertEqual(root.children[0].data, 2)
        self.assertEqual(root.children[1].data, 3)
        self.assertEqual(len(root.children[0].children), 2)
        self.assertEqual(root.children[0].children[0].data, 4)
        self.assertEqual(root.children[0].children[1].data, 5)
        self.assertEqual(len(root.children[1].children), 2)
        self.assertEqual(root.children[1].children[0].data, 6)
        self.assertEqual(root.children[1].children[1].data, 7)

if __name__ == '__main__':
    unittest.main()
