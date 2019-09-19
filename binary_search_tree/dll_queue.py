
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        # enqueue should add an item to the back of the queue.
        self.size += 1
        self.storage.add_to_head(value)

    def dequeue(self):
        # dequeue should remove and return an item from the front of the queue.
        if self.size >= 1:
            self.size -= 1
            return self.storage.remove_from_tail()
        else:
            return

    def len(self):
        # len returns the number of items in the queue.
        return self.size
