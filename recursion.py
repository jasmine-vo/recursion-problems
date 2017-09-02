
#################################################
### Write a function to check if BST is valid ###
#################################################

class Node:
    """Binary search tree node."""

    def __init__(self, data, left=None, right=None):
        """Create node, with data and optional left/right."""

        self.left = left
        self.right = right
        self.data = data
    
def is_valid(node, mini=None, maxi=None):
    """Is this tree a valid BST?"""

    if node is None:
        return True

    if maxi is not None and node.data > maxi:
        return False

    if mini is not None and node.data < mini:
        return False
    
    return is_valid(node.left, mini, node.data) and is_valid(node.right, node.data, maxi)