class Solution:
    def sum_leaves(self, node):
        if not (node.left or node.right):
            return [node.val]
        
        val = []
        if node.left:
            val.extend(self.sum_leaves(node.left))
        if node.right:
            val.extend(self.sum_leaves(node.right))
        return val
        
    
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leaves_1 = self.sum_leaves(root1)
        leaves_2 = self.sum_leaves(root2)
        if len(leaves_1) != len(leaves_2):
            return False
        for i in range(len(leaves_1)):
            if leaves_1[i] != leaves_2[i]:
                return False
            
        return True
