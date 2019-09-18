

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # if passed in value < self.value:
        if value < self.value:
            # if self.left is none, it means there are no
            if self.left == None:
                self.left = BinarySearchTree(value)
            # numbers smaller, so i can make a new BST with value. essentially making self.left an instance of BST.
            # else: if there is a node on self.left:
            else:
                # i can just make self.left the new 'root' and
                # since it an instance of BST it has access to insert method  call insert and have it loop through these steps again
                self.left.insert(value)
        # Else: if value > self.value:
        else:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
            # i can do the opposite of above code

    def contains(self, target):
        if target == self.value:
            return True
        else:
            if target < self.value:
                if self.left == None:
                    return False
                else:
                    return self.left.contains(target)
            else:
                if self.right == None:
                    return False
                else:
                    return self.right.contains(target)

    def get_max(self):
        # for max we want to check the leaves becasue we now there are no values after that. so if self.right has no value it means that there are no more larger numbers so it can return itself.
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()

    def for_each(self, cb):
        cb(self.value)
        if self.left != None:
            self.left.for_each(cb)
        if self.right != None:
            self.right.for_each(cb)


# * Should have the methods `insert`, `contains`, `get_max`.
# * `insert` adds the input value to the binary search tree, adhering to the rules of the ordering of elements in a binary search tree.
# * `contains` searches the binary search tree for the input value, returning a boolean indicating whether the value exists in the tree or not.
# * `get_max` returns the maximum value in the binary search tree.
# * `for_each` performs a traversal of _every_ node in the tree, executing the passed-in callback function on each tree node value. There is a myriad of ways to perform tree traversal
# in this case any of them should work.
