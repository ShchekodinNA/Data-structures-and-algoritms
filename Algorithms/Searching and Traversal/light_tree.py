class BNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = BNode(value)
        else:
            cur_node = self.root
            while True:
                if value > cur_node.value:
                    if cur_node.right:
                        cur_node = cur_node.right
                    else:
                        cur_node.right = BNode(value)
                        return
                elif value < cur_node.value:
                    if cur_node.left:
                        cur_node = cur_node.left
                    else:
                        cur_node.left = BNode(value)
                        return
                else:
                    return

    def lookup(self, value):
        if not self.root:
            return None
        cur_node = self.root
        while cur_node:
            if value > cur_node.value:
                cur_node = cur_node.right
            elif value < cur_node.value:
                cur_node = cur_node.left
            else:
                return cur_node
