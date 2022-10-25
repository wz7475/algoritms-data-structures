from trees.avl import AVLNode, AVLTree

import pytest


def test_avl_create():
    values = [2, 1, 4, 6, 0]
    avl = AVLTree(values)
    assert avl.root.value == 2
    assert avl.root.left_child.value == 1
    assert avl.root.left_child.left_child.value == 0
    assert avl.root.right_child.value == 4
    assert avl.root.right_child.right_child.value == 6


def test_avl_duplicate():
    values = [12, 3, 4, 45, 3]
    with pytest.raises(ValueError):
        AVLTree(values)


def test_avl_search():
    values = [2, 1, 4, 6, 0]
    avl = AVLTree(values)
    assert avl.root.value == 2
    assert avl.root.left_child.value == 1
    assert avl.root.left_child.left_child.value == 0
    assert avl.root.right_child.value == 4
    assert avl.root.right_child.right_child.value == 6

    for value in values:
        assert avl.search(value)

    for value in [3, 7, -8, 100]:
        assert not avl.search(value)


def test_avl_delete_leaf():
    values = [10, 5, 15, 2, 6, 17, 12]
    avl = AVLTree(values)
    avl.delete(17)
    assert avl.root.right_child.right_child is None


def test_avl_delete_only_child():
    values = [10, 5, 15, 2, 6, 12]
    avl = AVLTree(values)
    avl.delete(15)
    assert avl.root.right_child.value == 12
    assert avl.root.right_child.left_child is None
    assert avl._find(15) is None


def test_avl_delete_two_children():
    values = [10, 5, 15, 2, 6, 17, 12]
    avl = AVLTree(values)
    avl.delete(15)
    assert avl.root.right_child.value == 17
    assert avl.root.right_child.left_child.value == 12
    assert avl.root.right_child.right_child is None
    assert avl._find(15) is None
