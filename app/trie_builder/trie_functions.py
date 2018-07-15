"""functions.py

The following file contains a collection of functions for the trie structure search engine

"""

from typing import List, Tuple
from .Node import Node


def look_for_words_beginning_with_prefix(node: Node, prefix: str) -> List[str]:
    """
    Takes a prefix string and searches a trie for words

    Params:
        node (Node): A root node representing the root of a Trie structure
        prefix(str): A str containing the prefix of a desired search word

    Returns:
        results (List[str]): A list of words beginning with the prefix requested

    """

    original = node
    results = []

    for char in prefix:
        child_node = find_matching_child_node(node, char)
        if child_node:
            node = child_node
        else:
            return results

    if node != original:
        endings_list = look_for_words(node)
        prepended_words = list(map(lambda s: prefix + s, endings_list))
        results += prepended_words

    return results


def look_for_ranked_words_beginning_with_prefix(node: Node, prefix: str) -> List[Tuple[str, int]]:
    """
    Takes a prefix string and searches a trie for words

    Params:
        node (Node): A root node representing the root of a Trie structure
        prefix(str): A str containing the prefix of a desired search word

    Returns:
        results (List[str]): A list of words beginning with the prefix requested

    """

    original = node
    results = []

    for char in prefix:
        child_node = find_matching_child_node(node, char)
        if child_node:
            node = child_node
        else:
            return results

    if node != original:
        endings_list = look_for_words_with_count(node)
        prepended_words = list(map(lambda n: (prefix + n[0], n[1]), endings_list))
        results += prepended_words

    return sorted(results, key=lambda x: x[1], reverse=True)


def find_matching_child_node(node: Node, char: str) -> Node:
    """
    Finds a child node from the node's list of children that contains the matching search character


    Params:
        node (Node): The node to start searching from
        char (str): The search character

    Returns:
        A node instances containing the letter, otherwise None.

    """

    child_letters = check_children_letters(node)
    if char in child_letters:
        child_index = child_letters.index(char)
        return node.children[child_index]
    return None


def look_for_words(node: Node, accumulated: str = "") -> List[str]:
    """
    Recursively searches for all words in a trie structure. Base condition returns if the
    last letter actually creates a word. Continues to recursively search for more words
    if child nodes exist.

    Params:
        node (Node): Any node within a trie structure
        accumulated: A str containing letters gathered from higher parents

    Returns:
        results (List[str]): A list of words
    """

    results = []

    if node.is_a_word:
        results += [accumulated]

    if len(node.children) > 0:
        for child in node.children:
            results += look_for_words(child, accumulated + child.letter)
    return results


def look_for_words_with_count(node: Node, accumulated: str = "") -> List[str]:
    """
    Recursively searches for all words in a trie structure. Base condition returns if the
    last letter actually creates a word. Continues to recursively search for more words
    if child nodes exist.

    Params:
        node (Node): Any node within a trie structure
        accumulated: A str containing letters gathered from higher parents

    Returns:
        results (List[str]): A list of words
    """

    results = []

    if node.is_a_word:
        results += [(accumulated, node.count)]

    if len(node.children) > 0:
        for child in node.children:
            results += look_for_words_with_count(child, accumulated + child.letter)
    return results


def create_root_node():
    """
    Create a root node representing the root node of a trie

    Returns:
        Node: an Node instance containing representing an empty Trie

    """
    return Node("*")


def check_children_letters(node: Node):
    """
    Returns a list of strings representing the letters for each child node in the list passed in

    Params:
        node (Node): A node to check

    Returns:
        list_(List[Node]): A list of characters for each Node
    """
    return list(map(lambda s: s.letter, node.children))


def get_child_node(parent: Node, char: str) -> Node:
    """
    TODO: Finish definition
    """

    filtered = list(filter(lambda s: s.letter == char, parent.children))
    return filtered[0]


def add_word_to_trie(node: Node, word: str, definition: str, count: int = None):
    """
    Adds a new word to the trie structure

    Params:
        list_(List[Node]):

    Returns:
        SOMETHING TODO

    """
    for char in word:
        children_letters = check_children_letters(node)
        if char not in children_letters:
            node.children += [Node(char)]
        child_node = get_child_node(node, char)
        node = child_node
    node.is_a_word = True
    node.definition = definition
    node.count = count


def update_definition(root, word, new_definition) -> Node:
    """

    Updates a term within an existing trie with a new definition

    Params:
        root (Node): The existing trie
        word (str): the term of which the definition is to be updated
        new_definition (str): the new definition for the term

    Returns:
        A Node object representing the new trie containing the term with the new definition, else returns None

    """

    node = root
    for char in word:
        if char not in check_children_letters(node):
            return None
        node = get_child_node(node, char)
    if node.is_a_word and node.definition != "":
        node.definition = new_definition
        return root
    else:
        return None


def find_definition(root, word: str):
    """
    Updates a term within an existing trie with a new definition

    Params:
        root (Node): A trie containing words
        word (str): The term for the definition to be found

    Returns:
        Returns the a string contaiining the definition, otherwise None

    """

    node = root
    for char in word:
        if char not in check_children_letters(node):
            return None
        node = get_child_node(node, char)
    if node.is_a_word:
        return node.definition
    else:
        return None


def find_prefix(root, prefix: str):
    """
    TODO:
    """

    node = root
    for char in prefix:
        if char not in check_children_letters(node):
            return False
        node = get_child_node(node, char)
    return True
