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

    def remove(self,value ):               # later
        if not self.root:
            return False
        cur_node = self.root
        par_node = None
        while cur_node:
            if value > cur_node.value:
                par_node = cur_node
                cur_node = cur_node.right
            elif value < cur_node.value:
                par_node = cur_node
                cur_node = cur_node.left
            else:
                pass
                if cur_node.right and cur_node.left:
                    add_node = cur_node.right
                    while True:
                        if add_node.left:
                            add_node = add_node.left
                        else:
                            break
                    buf = add_node.value
                    self.remove(buf)
                    cur_node.value = buf
                elif cur_node.right:
                    if self.__is_child_right(par_node,cur_node):
                        par_node.right = cur_node.right
                    else:
                        par_node.left = cur_node.right
                elif cur_node.left:
                    if self.__is_child_right(par_node, cur_node):
                        par_node.right = cur_node.left
                    else:
                        par_node.left = cur_node.left
                else:
                    self.__del_node(par_node, cur_node)
                return True
        return False

    def __del_node(self,parent, child_to_delete):
        if self.__is_child_right(parent,child_to_delete):
            parent.right = None
        else:
            parent.left = None

    def __is_child_right(self,parent,child):
        if parent.left == child:
            return False
        return True
#       9
#   4       20
# 1   6  15   170

bst = BinarySearchTree()
bst.insert(9)
bst.insert(4)
bst.insert(20)
bst.insert(1)
bst.insert(6)
bst.insert(15)
bst.insert(170)
bst.insert(7)

print(bst.remove(4))
print("test")