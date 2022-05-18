import bstsize

class BST(bstsize.BST):
    """
    Adds select method to BST, starting with code from bstsize.
    """

    def select(self, index):
        """
        Takes a 1-based index, and returns the element at that index,
        or None if the index is out-of-bounds. Starting at the root,
        the tree is searched by examining the size of the left-child
        tree, which gives the number of elements smaller than the
        current node.
        """
        node = self.root
        if node==None: # if the tree is empty return None
            return None
        if index==0 or index > bstsize.size(node): # if elements dont exist in tree return None
            return None
        while True:


                left_count = bstsize.size(node.left) # count number of nodes
                right_count = bstsize.size(node.right)
                if index == left_count + 1:
                    return node
                elif index <= left_count:
                    node=node.left
                else:
                    node=node.right
                    index= index- left_count-1
