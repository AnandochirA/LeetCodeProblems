class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Trie:
    def __init__(self):
        self.root = TreeNode(None)  # Initialize root with None

    def insert(self, word: str) -> None:
        self._insert(word, self.root)  # Call recursive insert with root node

    def _insert(self, word: str, root: 'TreeNode') -> None:
        if root.val is None:  # If root is None (first insertion)
            root.val = word
            return

        if root.val == word:
            return  # Word is already inserted

        if root.val and root.val > word:  # Insert in left subtree
            if not root.left:
                root.left = TreeNode(word)  # Create new node if left child is None
            else:
                self._insert(word, root.left)  # Recur to left subtree
        elif root.val and root.val < word:  # Insert in right subtree
            if not root.right:
                root.right = TreeNode(word)  # Create new node if right child is None
            else:
                self._insert(word, root.right)  # Recur to right subtree

    def search(self, word: str) -> bool:
        return self._search(word, self.root)  # Call recursive search

    def _search(self, word: str, root: 'TreeNode') -> bool:
        if not root:
            return False  # If no more nodes to check, return False
        if root.val == word:
            return True  # If the word matches, return True
        if root.val and root.val > word:
            return self._search(word, root.left)  # Search in the left subtree
        elif root.val and root.val < word:
            return self._search(word, root.right)  # Search in the right subtree
        return False

    def startsWith(self, prefix: str) -> bool:
        return self._startsWith(prefix, self.root)  # Call recursive startsWith

    def _startsWith(self, prefix: str, root: 'TreeNode') -> bool:
        if not root:
            return False  # If no more nodes to check, return False
        if root.val and root.val.startswith(prefix):
            return True  # If the current node starts with the prefix, return True
        if root.val and root.val > prefix:
            return self._startsWith(prefix, root.left)  # Search in the left subtree
        elif root.val and root.val < prefix:
            return self._startsWith(prefix, root.right)  # Search in the right subtree
        return False


# Example Usage:
obj = Trie()
obj.insert("apple")
print(obj.search("apple"))  # True
print(obj.startsWith("app"))  # True
print(obj.search("app"))  # False
obj.insert("app")
print(obj.search("app"))  # True
