# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._push_left(root)

    def _push_left(self, node: Optional[TreeNode]):
        # dorong semua node kiri ke dalam stack
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        # ambil node paling atas (in-order terkecil berikutnya)
        node = self.stack.pop()
        val = node.val
        # setelah visit node, push semua subtree kanan-kirinya
        if node.right:
            self._push_left(node.right)
        return val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Example of usage:
# obj = BSTIterator(root)
# while obj.hasNext():
#     print(obj.next())
