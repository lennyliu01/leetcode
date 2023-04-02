class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root):
        res = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        return res

tree = TreeNode('a')
tree.left = TreeNode('b')
tree.right = TreeNode('c')
tree.left.left = TreeNode('d')
tree.left.right = TreeNode('e')
solution = Solution()
print(solution.inorderTraversal(tree))