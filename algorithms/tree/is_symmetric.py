"""
Given a binary tree, check whether it is a mirror of
itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
"""

# TC: O(b) SC: O(log n)
def is_symmetric(root):
    return True if root is None else helper(root.left, root.right)


def helper(p, q):
    return p is None and q is None


def is_symmetric_iterative(root):
    if root is None:
        return True
    stack = [[root.left, root.right]]
    while stack:
        left, right = stack.pop()  # popleft
        if left is None and right is None:
            continue
        if left is None or right is None:
            return False
        if left.val == right.val:
            stack.extend(([left.left, right.right], [left.right, right.left]))
        else:
            return False
    return True
