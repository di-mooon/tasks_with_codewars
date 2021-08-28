class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n


def tree_by_levels(node):
    lst = []
    
    def height(node):
        if not node:
            return 0
        height_left = height(node.left)
        height_right = height(node.right)
        return max(height_left, height_right) + 1

    def append_level(node, level):
        if not node:
            return
        elif level == 0:
            lst.append(node.value)

        elif level > 0:
            append_level(node.left, level - 1)
            append_level(node.right, level - 1)

    h = height(node)
    for i in range(h):
        append_level(node, i)

    return lst



