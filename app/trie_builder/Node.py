"""Node.py"""


class Node:
    """
    Node of the trie data structure
    """

    def __init__(self, letter: str, definition: str = "", count: int = 0):
        self.letter = letter
        self.children = []
        self.is_a_word = False
        self.definition = definition
        self.count = count
