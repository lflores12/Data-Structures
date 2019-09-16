Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?
   the runtime of 'enqueue' is O(1)

2) What is the runtime complexity of `dequeue`?
   The runtime of 'dequeue' is O(1)
3) What is the runtime complexity of `len`?
   O(1)

## Binary Search Tree

1. What is the runtime complexity of `insert`?

2. What is the runtime complexity of `contains`?

3. What is the runtime complexity of `get_max`?

## Heap

1. What is the runtime complexity of `_bubble_up`?

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?
   O(1)
2. What is the runtime complexity of `ListNode.insert_before`?
   O(1)
3. What is the runtime complexity of `ListNode.delete`?
   O(1)
4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?
   O(1)
5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
   O(1)
6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
   O(1)
7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
   O(1)
8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?
   O(1)
9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?
   O(1)
10. What is the runtime complexity of `DoublyLinkedList.delete`?

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?

    the delete method on 'DoublyLinkedList' is O(1) since its only changing the next and previous of one node at a time. And the runtime of 'splice' is O(n) because depending on how much of the array we want to splice will determine how many times we have to iterate over the array.
