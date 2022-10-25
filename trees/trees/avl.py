class AVLNode:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None
        self.height = 1


class AVLTree:
    def __init__(self, values=None):
        self.root = None
        if values is not None:
            self._create_tree(values)

    def _create_tree(self, values):
        for value in values:
            self.insert(value)

    def insert(self, value):
        if self.root is None:
            self.root = AVLNode(value)
        else:
            self._insert_helper(value, self.root)

    def _insert_helper(self, value, current_node):
        if value < current_node.value:
            if current_node.left_child is None:
                current_node.left_child = AVLNode(value)
                current_node.left_child.parent = current_node
                self._check_insert(current_node.left_child)
            else:
                self._insert_helper(value, current_node.left_child)
        elif value > current_node.value:
            if current_node.right_child is None:
                current_node.right_child = AVLNode(value)
                current_node.right_child.parent = current_node
                self._check_insert(current_node.right_child)
            else:
                self._insert_helper(value, current_node.right_child)
        else:
            raise ValueError("duplicate of value")

    def _find(self, value):
        if self.root is not None:
            return self._find_helper(value, self.root)
        else:
            return None

    def _find_helper(self, value, current_node):
        if value == current_node.value:
            return current_node
        elif value < current_node.value and current_node.left_child is not None:
            return self._find_helper(value, current_node.left_child)
        elif value > current_node.value and current_node.right_child is not None:
            return self._find_helper(value, current_node.right_child)

    def delete(self, value):
        return self._delete_node(self._find(value))

    def _delete_node(self, node_to_delete):
        if node_to_delete is None or self._find(node_to_delete.value) is None:
            raise ValueError("non existing")

        def min_value_node(node):
            current = node
            while current.left_child is not None:
                current = current.left_child
            return current

        # returns the number of children for the specified node
        def _number_of_children(node):
            num_children = 0
            if node.left_child is not None:
                num_children += 1
            if node.right_child is not None:
                num_children += 1
            return num_children

        node_parent = node_to_delete.parent

        node_children = _number_of_children(node_to_delete)

        # leaf
        if node_children == 0:
            if node_parent is not None:
                # remove reference to the node from the parent
                if node_parent.left_child == node_to_delete:
                    node_parent.left_child = None
                else:
                    node_parent.right_child = None
            else:
                self.root = None

        # single child
        if node_children == 1:
            # get child
            if node_to_delete.left_child is not None:
                child = node_to_delete.left_child
            else:
                child = node_to_delete.right_child

            # replace node_to_delete with child
            if node_parent is not None:
                if node_parent.left_child == node_to_delete:
                    node_parent.left_child = child
                else:
                    node_parent.right_child = child
            else:
                self.root = child

            child.parent = node_parent

        # 2 children
        if node_children == 2:
            successor = min_value_node(node_to_delete.right_child)

            # copy successor value to node_to_delete
            node_to_delete.value = successor.value

            # repeat procedure recursively
            self._delete_node(successor)

            return

        if node_parent is not None:
            node_parent.height = 1 + max(self._height(node_parent.left_child),
                                         self._height(node_parent.right_child))

            self._check_delete(node_parent)

    def search(self, value):
        if self.root is not None:
            return self._search_helper(value, self.root)
        else:
            return False

    def _search_helper(self, value, current_node):
        if value == current_node.value:
            return True
        elif value < current_node.value and current_node.left_child is not None:
            return self._search_helper(value, current_node.left_child)
        elif value > current_node.value and current_node.right_child is not None:
            return self._search_helper(value, current_node.right_child)
        return False

    def _check_insert(self, current_node, path=[]):
        # base case for recursion
        if current_node.parent is None:
            return
        path = [current_node] + path

        left_height = self._height(current_node.parent.left_child)
        right_height = self._height(current_node.parent.right_child)

        # if imbalance -> rebalance
        if abs(left_height - right_height) > 1:
            path = [current_node.parent] + path
            self._rebalance(path[0], path[1], path[2])
            # prevent multiple rebalance
            return

        # update height
        new_height = 1 + current_node.height
        if new_height > current_node.parent.height:
            current_node.parent.height = new_height

        # recursively check all higher nodes
        self._check_insert(current_node.parent, path)

    def _check_delete(self, node_to_delete):
        # leaf case
        if node_to_delete is None:
            return

        left_height = self._height(node_to_delete.left_child)
        right_height = self._height(node_to_delete.right_child)

        # if imbalance -> rebalance
        if abs(left_height - right_height) > 1:
            node_to_delete_child = self._taller_child(node_to_delete)
            node_to_delete_child_child = self._taller_child(node_to_delete_child)
            self._rebalance(
                node_to_delete,
                node_to_delete_child,
                node_to_delete_child_child
            )

        self._check_delete(node_to_delete.parent)

    def _rebalance(self, top_node, child, child_child):
        # LL case
        if child == top_node.left_child and child_child == child.left_child:
            self._right_rotate(top_node)
        # LR case
        elif child == top_node.left_child and child_child == child.right_child:
            self._left_rotate(child)
            self._right_rotate(top_node)
        # RR case
        elif child == top_node.right_child and child_child == child.right_child:
            self._left_rotate(top_node)
        # RL case
        elif child == top_node.right_child and child_child == child.left_child:
            self._right_rotate(child)
            self._left_rotate(top_node)

    def _right_rotate(self, top_node):
        sub_root = top_node.parent
        child = top_node.left_child
        child_tree = child.right_child
        child.right_child = top_node
        top_node.parent = child
        top_node.left_child = child_tree
        if child_tree is not None:
            child_tree.parent = top_node
        child.parent = sub_root
        if child.parent is None:
            self.root = child
        else:
            if child.parent.left_child == top_node:
                child.parent.left_child = child
            else:
                child.parent.right_child = child
        top_node.height = 1 + max(self._height(top_node.left_child),
                                  self._height(top_node.right_child))
        child.height = 1 + max(self._height(child.left_child),
                               self._height(child.right_child))

    def _left_rotate(self, top_node):
        sub_root = top_node.parent
        child = top_node.right_child
        child_tree = child.left_child
        child.left_child = top_node
        top_node.parent = child
        top_node.right_child = child_tree
        if child_tree is not None:
            child_tree.parent = top_node
        child.parent = sub_root
        if child.parent is None:
            self.root = child
        else:
            if child.parent.left_child == top_node:
                child.parent.left_child = child
            else:
                child.parent.right_child = child
        top_node.height = 1 + max(self._height(top_node.left_child),
                                  self._height(top_node.right_child))
        child.height = 1 + max(self._height(child.left_child),
                               self._height(child.right_child))

    def _height(self, current_node):
        if current_node is None:
            return 0
        return current_node.height

    def _taller_child(self, current_node):
        left = self._height(current_node.left_child)
        right = self._height(current_node.right_child)
        return current_node.left_child if left >= right else current_node.right_child

    def __str__(self):
        if self.root is None:
            return ''
        content = ''
        current_nodes = [self.root]  # all nodes at current level
        current_height = self.root.height  # height of nodes at current level
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

                if current_node.value is not None:
                    margin = ' ' * int((5 - len(str(current_node.value))) / 2)
                    current_row += f'{margin}{str(current_node.value)}{margin}{space}'
                else:
                    current_row += ' ' * 5 + space

                if current_node.left_child is not None:
                    next_nodes.append(current_node.left_child)
                    next_row += ' /' + space
                else:
                    next_row += '  ' + space
                    next_nodes.append(None)

                if current_node.right_child is not None:
                    next_nodes.append(current_node.right_child)
                    next_row += '\ ' + space
                else:
                    next_row += '  ' + space
                    next_nodes.append(None)

            content += (current_height * '   ' + current_row + '\n' + current_height * '   ' + next_row + '\n')
            current_nodes = next_nodes
            space = ' ' * int(len(space) / 2)  # cut separator size in half
        return content
