from dll_queue import Queue
from dll_stack import Stack


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
        # for max we want to check the leaves because we now there are no values after that. so if self.right has no value it means that there are no more larger numbers so it can return itself.
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

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_dft(self, node):
        if node.left:
            node.in_order_dft(node.left)
        print(node.value)
        if node.right:
            node.in_order_dft(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    # Breadth first search - queue

        # check each level one at a time

        # create a queue
        # put root in queue
        # while queue is not empty
        # pop first item in queue
        # check left and right add to queue
        # shift
        # go to head of queue and continue
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)
        while queue.size != 0:
            dequeued = queue.dequeue()
            print(dequeued.value)
            if dequeued.left:
                queue.enqueue(dequeued.left)
            if dequeued.right:
                queue.enqueue(dequeued.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        # create a stack
        stack = Stack()
        # put root in stack
        stack.push(node)
    # while stack is not empty
        while stack.size != 0:
            # pop first item in stack
            popped = stack.pop()
            print(popped.value)
        # check root.left and put it in stack
            if popped.right:
                stack.push(popped.right)
        # check root.right and put it in stack
            if popped.left:
                stack.push(popped.left)
        # go to top of stack and continue

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


test = BinarySearchTree(7)
test.insert(5)
test.insert(2)
test.insert(9)
test.insert(21)
test.insert(30)
test.insert(1)
test.insert(10)
test.in_order_dft(test)
