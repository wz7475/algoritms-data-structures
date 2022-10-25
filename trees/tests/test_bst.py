from trees.bst import BST, BSTNode
import pytest
from random import randint
import sys


# Tests for height()

def test_height():
    bst = BST(10)
    assert bst.root().height() == 0
    
    bst.insert(5)
    bst.insert(15)

    assert bst.root().height() == 1

    bst.insert(2)
    bst.insert(1)

    assert bst.root().height() == 3

    bst.insert(20)
    bst.insert(7)

    assert bst.root().height() == 3

# Tests for insert()

def test_insert_only_root():
    bst = BST(20)
    bst.insert(10)
    bst.insert(30)

    assert bst.root().left().value() == 10
    assert bst.root().right().value() == 30


def test_insert_multiple_level():
    bst = BST(0)
    bst.insert(-1)
    bst.insert(-20)
    bst.insert(30)
    bst.insert(10)
    bst.insert(20)

    assert bst.root().left().value() == -1
    assert bst.root().left().left().value() == -20
    assert bst.root().right().value() == 30
    assert bst.root().right().left().value() == 10
    assert bst.root().right().left().right().value() == 20


def test_insert_existing_item():
    bst = BST(10)
    bst.insert(12)
    bst.insert(-20)

    with pytest.raises(ValueError):
        bst.insert(-20)

    with pytest.raises(ValueError):
        bst.insert(12)

    with pytest.raises(ValueError):
        bst.insert(10)


# Tests for indexing

def test_index():
    bst = BST(0)
    bst.insert(-1)
    bst.insert(-20)
    bst.insert(30)
    bst.insert(10)
    bst.insert(20)

    assert bst.root().index() == 1
    assert bst.root().left().index() == 2
    assert bst.root().left().left().index() == 4
    assert bst.root().right().index() == 3
    assert bst.root().right().left().index() == 6
    assert bst.root().right().left().right().index() == 13


# Tests for find()

def test_find_typical():
    bst = BST(0)
    bst.insert(-1)
    bst.insert(-20)
    bst.insert(30)
    bst.insert(10)
    bst.insert(20)

    assert bst.find(0) == 1
    assert bst.find(-1) == 2
    assert bst.find(-20) == 4
    assert bst.find(30) == 3
    assert bst.find(10) == 6
    assert bst.find(20) == 13


def test_find_non_existing():
    bst = BST(0)
    bst.insert(-1)
    bst.insert(-20)
    bst.insert(30)
    bst.insert(10)
    bst.insert(20)

    with pytest.raises(ValueError):
        bst.find(2)

    with pytest.raises(ValueError):
        bst.find(21)


# Tests for fill()

def test_fill():
    bst = BST(10)
    numbers = []
    sys.setrecursionlimit(10000)

    while len(numbers) < 10000:
        number = randint(-30000, 30000)

        if number != 10 and number not in numbers:
            numbers.append(number)

    bst.fill(numbers)
    pass


# Tests for delete()

def test_delete_leaf():
    bst = BST(10)
    bst.insert(2)
    bst.remove(2)

    assert bst.root().is_leaf()


def test_delete_single_child():
    bst = BST(10)
    bst.insert(2)
    bst.insert(20)
    bst.insert(5)
    bst.insert(7)
    bst.insert(3)

    bst.remove(2)

    assert bst.root().left().value() == 5
    assert bst.root().left().left().value() == 3
    assert bst.root().left().right().value() == 7
    assert bst.root().right().value() == 20

    assert bst.root().left().index() == 2
    assert bst.root().left().left().index() == 4
    assert bst.root().left().right().index() == 5
    assert bst.root().right().index() == 3


def test_delete_two_children():
    bst = BST(8)
    bst.insert(3)
    bst.insert(10)
    bst.insert(14)
    bst.insert(1)
    bst.insert(6)
    bst.insert(4)
    bst.insert(7)

    bst.remove(3)

    assert bst.root().left().value() == 4
    assert bst.root().left().left().value() == 1
    assert bst.root().left().right().value() == 6
    assert bst.root().left().right().right().value() == 7
    assert bst.root().left().right().left() is None

    assert bst.root().index() == 1
    assert bst.root().left().index() == 2
    assert bst.root().right().index() == 3
    assert bst.root().left().left().index() == 4
    assert bst.root().left().right().index() == 5
    assert bst.root().left().right().right().index() == 11
    assert bst.root().right().right().index() == 7


def test_delete_root_with_one_child():
    bst = BST(10)
    bst.insert(20)
    bst.insert(15)
    bst.insert(30)

    bst.remove(10)

    assert bst.root().value() == 20
    assert bst.root().left().value() == 15
    assert bst.root().right().value() == 30

    assert bst.root().index() == 1
    assert bst.root().left().index() == 2
    assert bst.root().right().index() == 3


def test_delete_root_with_two_children():
    bst = BST(10)
    bst.insert(5)
    bst.insert(20)
    bst.insert(15)

    bst.remove(10)

    assert bst.root().value() == 15
    assert bst.root().left().value() == 5
    assert bst.root().right().value() == 20

    assert bst.root().index() == 1
    assert bst.root().left().index() == 2
    assert bst.root().right().index() == 3


def test_delete_wrong_values():
    bst = BST(10)
    bst.insert(2)
    bst.insert(20)

    with pytest.raises(ValueError):
        bst.remove(5)

    bst.remove(2)
    bst.remove(20)

    with pytest.raises(ValueError):
        bst.remove(10)
