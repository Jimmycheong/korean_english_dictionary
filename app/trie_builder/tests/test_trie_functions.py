"""functions.py

File containing tests for functions.py

"""
import pytest
from grappa import should

from app.trie_builder.Node import Node
from app.trie_builder.trie_functions import (
    create_root_node,
    find_definition,
    update_definition,
    add_word_to_trie,
    look_for_words_beginning_with_prefix,
    look_for_ranked_words_beginning_with_prefix,
    look_for_words,
    look_for_words_with_count,
    find_matching_child_node
)

'''FIXTURES '''

TEST_DICT = {
    "한": {
        "definition": "one",
        "count": 3
    },
    "한국": {
        "definition": "Korea",
        "count": 4
    },
    "왜": {
        "definition": "why",
        "count": 2
    },
    "이름": {
        "definition": "name",
        "count": 1
    }
}


@pytest.fixture
def prepopulated_trie():
    root = create_root_node()

    for word in TEST_DICT:
        add_word_to_trie(root, word,
                         TEST_DICT[word]["count"], TEST_DICT[word]["count"])  # FIX THE DEFINITION

    return root


'''
TESTS

'''


def test_look_for_words_beginning_with_prefix(prepopulated_trie):
    root = prepopulated_trie

    # Case where prefix displays all results
    results = look_for_words_beginning_with_prefix(root, "한")
    sorted(results) | should.be.equal.to(["한", "한국"])


def test_look_for_ranked_words_beginning_with_prefix(prepopulated_trie):
    root = prepopulated_trie

    results = look_for_ranked_words_beginning_with_prefix(root, "한")
    results | should.be.equal.to([("한국", 4), ("한", 3)])


def test_find_matching_child_node(prepopulated_trie):
    root = prepopulated_trie

    found_node = find_matching_child_node(root, "한")
    missing_node = find_matching_child_node(root, "국")

    # Happy path
    found_node.letter | should.be.equal.to("한")
    isinstance(found_node, Node) == True

    # Bad Case
    missing_node | should.be.equal.to(None)


def test_look_for_words(prepopulated_trie):
    root = prepopulated_trie

    results = look_for_words(root, "")

    results | should.be.equal.to(list(TEST_DICT.keys()))


def test_look_for_words_with_count(prepopulated_trie):
    root = prepopulated_trie

    results = look_for_words_with_count(root, "")

    expectations = [('한', 3), ('한국', 4), ('왜', 2), ('이름', 1)]

    results | should.be.equal.to(expectations)


def test_add_word_to_trie(prepopulated_trie):
    root = prepopulated_trie

    add_word_to_trie(root, "한국", "Korea")

    child_1 = get_single_child(root)
    child_1.letter | should.be.equal.to("한")

    child_2 = get_single_child(child_1)
    child_2.letter | should.be.equal.to("국")


def test_find_definition(prepopulated_trie):
    root = prepopulated_trie

    term = "행복하다"
    definition = "to be happy"

    add_word_to_trie(root, term, definition)

    found_definition = find_definition(root, term)
    no_definition = find_definition(root, "없은언어")

    found_definition | should.equal.to(definition)

    no_definition | should.equal.to(None)


def test_update_definition(prepopulated_trie):
    root = prepopulated_trie

    term = "어디"
    definition = "wear"

    add_word_to_trie(root, term, definition)

    new_definition = "where"

    root = update_definition(root, term, new_definition)

    found_definition = find_definition(root, term)
    found_definition | should.equal.to(new_definition)


'''TEST HELPER FUNCTIONS '''


def get_single_child(parent: Node):
    return parent.children[0]
