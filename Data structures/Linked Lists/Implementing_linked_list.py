class Node:
    def __init__(self, value):
        self.value =value
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        self.tail.next = Node(value)
        self.tail = self.tail.next
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
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
        ins_node.next = prev_node.next
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
            self.length -= 1
            return

        del_node = self.__traverse_to_index(index)
        del_node.next = del_node.next.next
        self.length -= 1

    def print_list(self):
        arr = []
        cur_node = self.head
        while cur_node:
            arr.append(cur_node.value)
            cur_node = cur_node.next
        return arr

    def reverse(self):
        if self.length < 2:
            return
        cur_node = self.head
        self.tail = self.head
        sec_node = cur_node.next
        while sec_node:
            sec_next = sec_node.next
            sec_node.next = cur_node
            cur_node = sec_node
            sec_node = sec_next
        self.tail.next = None
        self.head = cur_node


llist = LinkedList(2)

llist.append(4)
llist.append(8)
llist.prepend(1)

print(llist.print_list(), llist.length)
llist.reverse()
print(llist.print_list(), llist.length)