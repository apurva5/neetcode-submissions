# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def min_node(root):
            curr = root
            while curr and curr.left:
                curr = curr.left
            return curr
        def delete(root,key):
            if not root:
                return None
            if key > root.val:
                root.right = delete(root.right , key)
            elif key < root.val:
                root.left = delete(root.left , key)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                minNode = min_node(root.right)
                root.val = minNode.val
                root.right = delete(root.right,minNode.val)

            return root
        return delete(root,key)