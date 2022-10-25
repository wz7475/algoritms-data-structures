class BSTNode:
    def __init__(
            self, value: int, index: int = 1,
            left=None, right=None, parent=None) -> None:
        self.__index = index
        self.__value = value
        self.__left = left
        self.__right = right
        self.__parent = parent

    # Getters

    def index(self) -> int:
        return self.__index

    def value(self) -> int:
        return self.__value

    def left(self):
        return self.__left

    def right(self):
        return self.__right

    def parent(self):
        return self.__parent

    # Setters

    def set_left(self, value) -> None:
        self.__left = value

    def set_right(self, value) -> None:
        self.__right = value

    def set_value(self, value: int) -> None:
        self.__value = value

    def set_index(self, value: int) -> None:
        self.__index = value

    # Public methods

    def insert(self, value: int) -> None:
        if value > self.value():
            if self.__right is not None:
                self.__right.insert(value)
            else:
                self.__right = BSTNode(
                     value, self.__index * 2 + 1, parent=self)
        elif value < self.value():
            if self.__left is not None:
                self.__left.insert(value)
            else:
                self.__left = BSTNode(value, self.__index * 2, parent=self)
        else:
            raise ValueError("Cannot insert an existing item")

    def find(self, value: int):
        if value > self.__value:
            if self.__right is not None:
                return self.__right.find(value)
            else:
                raise ValueError("The tree does not contain the given value")
        elif value < self.__value:
            if self.__left is not None:
                return self.__left.find(value)
            else:
                raise ValueError("The tree does not contain the given value")
        else:
            return self

    # Helper methods

    def is_leaf(self) -> bool:
        return self.children_amount() == 0

    def children_amount(self) -> int:
        if self.__left is not None and self.__right is not None:
            return 2
        elif self.__left is None and self.__right is None:
            return 0
        else:
            return 1

    def recalculate_indexes(self) -> None:
        if self.__left is not None:
            self.__left.__index = self.__index * 2
            self.__left.recalculate_indexes()

        if self.__right is not None:
            self.__right.__index = self.__index * 2 + 1
            self.__right.recalculate_indexes()

    def minimal_child(self):
        if self.__left is not None:
            return self.__left.minimal_child()
        else:
            return self

    def height(self):
        if self.left() is None and self.right() is None:
            return 0
        elif self.left() is None:
            return self.right().height() + 1
        elif self.right() is None:
            return self.left().height() + 1
        else:
            return max(self.left().height() + 1, self.right().height() + 1)


class BST:
    def __init__(self, root_value: int) -> None:
        self.__root = BSTNode(root_value, 1)

    # Getters

    def root(self) -> BSTNode:
        return self.__root

    # Public methods

    def fill(self, numbers: list) -> None:
        for number in numbers:
            self.__root.insert(number)

    def insert(self, value: int) -> None:
        self.__root.insert(value)

    def find(self, value: int) -> int:
        return self.__root.find(value).index()

    def remove(self, value: int) -> None:
        if self.root().is_leaf():
            raise ValueError(
                "Cannot remove an item from a signle-element tree")

        node_to_remove = self.__root.find(value)
        removed_node_parent = node_to_remove.parent()

        if node_to_remove.is_leaf():
            self.__remove_leaf(node_to_remove, removed_node_parent)

        elif node_to_remove.children_amount() == 1:
            self.__remove_single_child(node_to_remove, removed_node_parent)

        else:
            self.__remove_two_children(node_to_remove, removed_node_parent)

    def __remove_leaf(
            self, node_to_remove: BSTNode,
            removed_node_parent: BSTNode) -> None:

        if node_to_remove.value() < removed_node_parent.value():
            removed_node_parent.set_left(None)
        else:
            removed_node_parent.set_right(None)

    def __remove_single_child(
            self, node_to_remove: BSTNode,
            removed_node_parent: BSTNode) -> None:

        # Replace the node with its child

        node_to_replace = (
            node_to_remove.left()
            if node_to_remove.left() is not None
            else node_to_remove.right())

        node_to_remove.__init__(
            node_to_replace.value(), node_to_replace.index(),
            node_to_replace.left(), node_to_replace.right(),
            node_to_replace.parent())

        if removed_node_parent is None:
            self.root().set_index(1)
            self.root().recalculate_indexes()
        else:
            removed_node_parent.recalculate_indexes()

    def __remove_two_children(
            self, node_to_remove: BSTNode,
            removed_node_parent: BSTNode) -> None:

        # Gets the inorder successor of the node to remove, swaps them
        # and removes the old node

        inorder_successor = node_to_remove.right().minimal_child()
        node_to_remove.set_value(inorder_successor.value())
        inorder_successor.parent().set_left(None)

        if removed_node_parent is None:
            self.root().set_index(1)
            self.root().recalculate_indexes()
        else:
            removed_node_parent.recalculate_indexes()

    def __str__(self) -> str:
        if self.root() is None:
            return ''
        content = ''
        current_nodes = [self.root()]  # all nodes at current level
        current_height = self.root().height()  # height of nodes at current level
        space = ' ' * (2 ** (current_height - 1))  # variable sized separator between elements
        while True:
            current_height += -1
            if len(current_nodes) == 0:
                break
            current_row = ' '
            next_row = ''
            next_nodes = []

            if all(n is None for n in current_nodes):
                break

            for current_node in current_nodes:
                if current_node is None:
                    current_row += '   ' + space
                    next_row += '   ' + space
                    next_nodes.extend([None, None])
                    continue

                if current_node.value() is not None:
                    margin = ' ' * int((5 - len(str(current_node.value()))) / 2)
                    current_row += f'{margin}{str(current_node.value())}{margin}{space}'
                else:
                    current_row += ' ' * 5 + space

                if current_node.left() is not None:
                    next_nodes.append(current_node.left())
                    next_row += ' /' + space
                else:
                    next_row += '  ' + space
                    next_nodes.append(None)

                if current_node.right() is not None:
                    next_nodes.append(current_node.right())
                    next_row += '\ ' + space
                else:
                    next_row += '  ' + space
                    next_nodes.append(None)

            content += (current_height * '   ' + current_row + '\n' + current_height * '   ' + next_row + '\n')
            current_nodes = next_nodes
            space = ' ' * int(len(space) / 2)  # cut separator size in half
        return content
