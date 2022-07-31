from light_tree import *


class DFSWithTree(BinarySearchTree):
    def __init__(self):
        super().__init__()

    def inorder(self):
        return self.__DFS_inord(self.root)

    def preorder(self):
        return self.__f_rec_dfs(self.root)

    def postorder(self):
        return self.__DFS_post(self.root)

    def __DFS_inord(self, node):
        if not BNode:
            return []
        if not node.right and not node.left:
            return [node.value]
        return self.__DFS_inord(node.left) + [node.value] + self.__DFS_inord(node.right)

    def __DFS_post(self, node):
        if not BNode:
            return []
        if not node.right and not node.left:
            return [node.value]
        return self.__DFS_post(node.left) + self.__DFS_post(node.right) + [node.value]

    def __f_rec_dfs(self, node: BNode):
        if not BNode:
            return []
        if not node.right and not node.left:
            return [node.value]

        return [node.value] + self.__f_rec_dfs(node.left) + self.__f_rec_dfs(node.right)


bst = DFSWithTree()
bst.insert(9)
bst.insert(4)
bst.insert(20)
bst.insert(1)
bst.insert(6)
bst.insert(15)
bst.insert(170)

print(f"PreOrder:   {bst.preorder()}")
print(f"InOrder:    {bst.inorder()}")
print(f"PostOrder:  {bst.postorder()}")
