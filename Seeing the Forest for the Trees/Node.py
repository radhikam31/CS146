class Node:
    def __init__(self, key, value, color):
        self.key = key
        self.value = value
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        if not self.root:
            self.root = Node(key, value, "BLACK")
            return

        node = self._insert(self.root, key, value)

        self._fix_insertion_violations(node)

    def _insert(self, root, key, value):
        if not root:
            return Node(key, value, "RED")

        if key < root.key:
            if not root.left:
                node = Node(key, value, "RED")
                root.left = node
                node.parent = root
                return node
            else:
                return self._insert(root.left, key, value)
        elif key > root.key:
            if not root.right:
                node = Node(key, value, "RED")
                root.right = node
                node.parent = root
                return node
            else:
                return self._insert(root.right, key, value)
        else:
            root.value = value
            return root

    def _fix_insertion_violations(self, node):
        while node != self.root and node.parent.color == "RED":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle and uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self._right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle and uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self._left_rotate(node.parent.parent)

        self.root.color = "BLACK"

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right:
            x.right.parent = y
        x.parent = y.parent
        if not y.parent:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, root, result):
        if root:
            self._inorder_traversal(root.left, result)
            result.append((root.key, root.value))
            self._inorder_traversal(root.right, result)

tree = RedBlackTree()
tree.insert(10, "A")
tree.insert(20, "B")
tree.insert(30, "C")
tree.insert(15, "D")
tree.insert(25, "E")
tree.insert(5, "F")

print("Inorder Traversal:", tree.inorder_traversal()) #Output: Inorder Traversal: [(5, 'F'), (10, 'A'), (15, 'D'), (20, 'B'), (25, 'E'), (30, 'C')]
