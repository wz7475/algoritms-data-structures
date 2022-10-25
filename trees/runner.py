from trees.avl import AVLTree
from trees.bst import BST

if __name__ == '__main__':

    values = [50, 40, 30, 45, 60, 55, 65, 25, 35, 42, 52, 57, 63, 67]
    tree = AVLTree(values)

    print(str(tree))

    tree.delete(50)

    print(str(tree))
    print("\n\nBST:\n\n")

    bst = BST(values[0])
    bst.fill(values[1:])

    print(str(bst))

    bst.remove(60)

    print(str(bst))
