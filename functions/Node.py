'''Node.py'''

class Node:
    """
    Node of the trie data structure
    """
    
    def __init__(self, letter: str, definition: str = ""):
        self.letter = letter
        self.children = []
        self.is_a_word = False
        self.defintion = definition
