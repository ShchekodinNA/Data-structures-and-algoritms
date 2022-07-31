from light_tree import *


class BFSWithTree(BinarySearchTree):
    def __init__(self):
        super().__init__()

    def bfs_iterative(self):
        cur_node = self.root
        rslt = []
        queue = []

        queue.append(cur_node)
        while len(queue) > 0:
            cur_node = queue[0]
            del queue[0]
            rslt.append(cur_node.value)
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)

        return rslt

    def bfs_recursive(self,queue:list,lst:list):
        if len(queue) < 1:
            return lst
        cur_node = queue.pop(0)
        lst.append(cur_node.value)
        if cur_node.left:
            queue.append(cur_node.left)
        if cur_node.right:
            queue.append(cur_node.right)

        return self.bfs_recursive(queue,lst)


#       9
#   4       20
# 1   6  15   170

bst = BFSWithTree()
bst.insert(9)
bst.insert(4)
bst.insert(20)
bst.insert(1)
bst.insert(6)
bst.insert(15)
bst.insert(170)

print(bst.bfs_iterative())
print(bst.bfs_recursive([bst.root],[]))