import pickle

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def save_tree(tree, filename='backup_tree.pickle'):
    with open(filename, 'wb') as f:
        pickle.dump(tree, f)

def load_tree(filename='backup_tree.pickle'):
    try:
        with open(filename, 'rb') as f:
            tree = pickle.load(f)
        return tree
    except (FileNotFoundError, pickle.UnpicklingError):
        return None

def insert_node(root, key):
    if root is None:
        return TreeNode(key)
    
    if key < root.key:
        root.left = insert_node(root.left, key)
    elif key > root.key:
        root.right = insert_node(root.right, key)

    return root

def search_node(root, key):
    if root is None or root.key == key:
        return root

    if key < root.key:
        return search_node(root.left, key)
    return search_node(root.right, key)

def delete_node(root, key):
    if root is None:
        return root

    if key < root.key:
        root.left = delete_node(root.left, key)
    elif key > root.key:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        root.key = find_min(root.right).key
        root.right = delete_node(root.right, root.key)

    return root

def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def inorder_traversal(root):
    result = []
    if root:
        result.extend(inorder_traversal(root.left))
        result.append(root.key)
        result.extend(inorder_traversal(root.right))
    return result

def clear_tree():
    return None

def main():
    backup_filename = 'backup_tree.pickle'
    tree = load_tree(backup_filename)

    while True:
        print("\nCommands:")
        print("add X - Add element to the tree")
        print("find X - Find element in the tree")
        print("delete X - Delete element from the tree")
        print("print - Print all elements in sorted order")
        print("clear - Clear the tree")
        print("dump - Create a backup of the tree")
        print("exit - Exit the program")

        command = input("Enter a command: ").split()

        if command[0] == 'add':
            value = int(command[1])
            tree = insert_node(tree, value)

        elif command[0] == 'find':
            value = int(command[1])
            result = search_node(tree, value)
            print(f"Element {value} found: {result is not None}")

        elif command[0] == 'delete':
            value = int(command[1])
            tree = delete_node(tree, value)

        elif command[0] == 'print':
            elements = inorder_traversal(tree)
            print("Tree elements:", elements)

        elif command[0] == 'clear':
            tree = clear_tree()
            print("Tree cleared.")

        elif command[0] == 'dump':
            save_tree(tree, backup_filename)
            print(f"Backup saved to {backup_filename}")

        elif command[0] == 'exit':
            break

if __name__ == "__main__":
    main()
