def invertTree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    def pre_order(node):

        # swap left and right
        node.left, node.right = node.right, node.left

        # traverse left
        if node.left:
            pre_order(node.left)

        # traverse right
        if node.right:
            pre_order(node.right)
    if root:
        pre_order(root)

    return root
