
from doubly_linked_list import DoublyLinkedList


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def __str__(self):
        return f'Size: {self.size},\nStorage: {self.storage}'

    def __repr__(self):
        return f'{self}'

    def push(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    def pop(self):
        if self.size >= 1:
            self.size -= 1
            self.storage.remove_from_head()
        else:
            return

    def len(self):
        return self.size


new_stack = Stack()
new_stack.push(5)
new_stack.push(6)
new_stack.pop()
print(new_stack)
