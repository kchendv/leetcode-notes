# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def helper(root):
                # No of good nodes / No of total nodes / Sum val
                if root.left == None and root.right == None:
                    # print(root.val, "leaf good")
                    return (1, 1, root.val)
                elif root.right == None:
                    l = helper(root.left)
                    if (l[2] + root.val) // (1 + l[1]) == root.val:
                        # print(root.val, "left good")
                        return(l[0] + 1,l[1] + 1,l[2] + root.val)
                    else:
                        # print(root.val, "left bad")
                        return(l[0],l[1] + 1,l[2] + root.val)
                elif root.left == None:
                    r = helper(root.right)
                    if (r[2] + root.val) // (1 + r[1]) == root.val:
                        # print(root.val, "right good")
                        return(r[0] + 1,r[1] + 1,r[2] + root.val)
                    else:
                        # print(root.val, "right bad")
                        return(r[0],r[1] + 1,r[2] + root.val)
                else:
                    l = helper(root.left)
                    r = helper(root.right)
                    if (l[2] + r[2] + root.val) // (1 + l[1] + r[1]) == root.val:
                        # print(root.val, "both good")
                        return(l[0] + r[0] + 1, l[1] + r[1] + 1, l[2] + r[2] + root.val)
                    else:
                        # print(root.val, "both bad")
                        return(l[0] + r[0], l[1] + r[1] + 1, l[2] + r[2] + root.val)
        return helper(root)[0]
            
        