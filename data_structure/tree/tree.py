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
