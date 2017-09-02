
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

    # if we reach None (the end of the tree), we know all conditions passed.
    if node is None:
        return True

    # the left children can't be greater than the parent (maximum number)
    if maxi is not None and node.data > maxi:
        return False

    # the right children can't be less than the parent (minimum number)
    if mini is not None and node.data < mini:
        return False
    
    # recurse on the left and right sides
    return is_valid(node.left, mini, node.data) and is_valid(node.right, node.data, maxi)


####################
### Flatten list ###
####################

def flatten(lst):
    """Given a nested list, returns a flattened list"""

    if lst == []:
        return lst

    if type(lst[0]) == list:
        return flatten(lst[0]) + flatten(lst[1:])

    return lst[:1] + flatten(lst[1:])


###############################################################################
### Given a number pad and a string, print all possible letter combinations ###
###############################################################################

"""
EX. number pad

num_pad = {'1': ['a', 'b', 'c'],
           '2': ['d', 'e', 'f'],
           '3': ['g', 'h', 'i']
           ....................
           }
continue & include 0-9

EX. string

str = '123'

will print:
adg
adh
adi
aeg
aeh
aei
afg
afh
afi
bdg
bdh
bdi
beg
beh
bei
bfg
bfh
bfi
cdg
cdh
cdi
ceg
ceh
cei
cfg
cfh
cfi
"""

def letter_combos(string, num_pad, idx=0, result=""):
    """ Given a number string and number pad, prints all possible letter
    combinations """

    if idx >= len(string) and len(result) > 0:
        print result
        return

    lst = num_pad.get(string[idx])

    for l in lst:
        letter_combos(string, num_pad, idx + 1, result + l)
