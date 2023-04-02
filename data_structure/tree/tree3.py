class Node:
    def __init__(self, value=None, first_child=None, next_sibling=None):
        self.value = value
        self.first_child = first_child
        self.next_sibling = next_sibling

class GeneralTree:
    def __init__(self, root=None):
        self.root = root
    
    def add_child(self, parent_node, child_value):
        new_child = Node(value=child_value)
        if not parent_node.first_child:
            parent_node.first_child = new_child
        else:
            current_child = parent_node.first_child
            while current_child.next_sibling:
                current_child = current_child.next_sibling
            current_child.next_sibling = new_child
    
    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        print("    " * level + str(node.value))
        child = node.first_child
        while child:
            self.print_tree(child, level + 1)
            child = child.next_sibling
    
    @classmethod
    def build_tree(cls, root_value, children_values):
        root = Node(value=root_value)
        tree = cls(root=root)
        for child_value in children_values:
            tree.add_child(root, child_value)
        return tree


root_value = 1
children_values = [2, 3, 4, 5]
tree = GeneralTree.build_tree(root_value, children_values)
parent = tree.root.first_child.next_sibling.next_sibling
tree.add_child(parent,6)
tree.print_tree()