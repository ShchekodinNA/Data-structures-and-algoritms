class Node:
    def __init__(self, value):
        self.value =value
        self.next = None
        self.prev = None                        # conversion


class DoublyLinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        self.tail.next = Node(value)
        self.tail.next.prev = self.tail                             # conversion
        self.tail = self.tail.next
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head.prev = new_node                                   # conversion
        self.head = new_node
        self.length += 1

    def insert(self, index, value):
        """
        If index bigger than length of LinkedList object, then method append will be executed.
        """
        if index >= self.length:
            self.append(value)
            return
        if index <= 0:
            self.prepend(value)
            return
        prev_node = self.__traverse_to_index(index)
        ins_node = Node(value)

        ins_node.prev = prev_node               # conversion
        ins_node.next = prev_node.next
        ins_node.next.prev = ins_node           # conversion
        prev_node.next = ins_node
        self.length += 1

    def __traverse_to_index(self, index):
        prev_node = self.head
        for i in range(index-1):
            prev_node = prev_node.next
        return prev_node

    def delete(self, index):
        if index >= self.length or index < 0:
            return
        if index == 0:
            self.head = self.head.next
            self.head.prev = None                   # conversion
            self.length -= 1
            return

        del_node = self.__traverse_to_index(index)
        del_node.next.next.prev = del_node              # conversion
        del_node.next = del_node.next.next
        self.length -= 1

    def print_list(self):
        arr = []
        cur_node = self.head
        while cur_node:
            arr.append(cur_node.value)
            cur_node = cur_node.next
        return arr



llist = DoublyLinkedList(10)

llist.append(20)
llist.append(15)
llist.prepend(5)
llist.insert(2, 50)
print(llist.print_list(), llist.length)
llist.delete(1)
print(llist.print_list(), llist.length)