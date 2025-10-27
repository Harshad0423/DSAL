class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        new_node = Node(key)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while True:
            if key < current.val:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    def search(self, key):
        current = self.root
        while current:
            if current.val == key:
                return current
            elif key < current.val:
                current = current.left
            else:
                current = current.right
        return None

    def level_order(self, root):
        if not root:
            return []
        queue = [root]
        result = []
        while queue:
            current = queue.pop(0)
            result.append(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result

    def display_leaf_nodes(self, root):
        if root:
            if not root.left and not root.right:
                print(root.val, end=' ')
            self.display_leaf_nodes(root.left)
            self.display_leaf_nodes(root.right)

def main():
    bst = BST()
    while True:
        print("\n1. Insert\n2. Search\n3. Display Leaf Nodes\n4. Level Order Traversal\n5. Exit")
        ch = int(input("Enter choice: "))
        if ch == 1:
            bst.insert(int(input("Enter value: ")))
        elif ch == 2:
            val = int(input("Enter value to search: "))
            print("Found" if bst.search(val) else "Not Found")
        elif ch == 3:
            print("Leaf Nodes:", end=' ')
            bst.display_leaf_nodes(bst.root); print()
        elif ch == 4:
            print("Level Order Traversal:", bst.level_order(bst.root))
        elif ch == 5:
            break
        else:
            print("Invalid choice")

main()
