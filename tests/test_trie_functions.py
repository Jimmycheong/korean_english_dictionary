'''functions.py 

File containing tests for functions.py

'''

# Access parent package
from sys import path
from os.path import dirname as dir
path.append(dir(path[0]))

from hanyongapp.functions.Node import Node
from hanyongapp.functions.trie_functions import (
	create_root_node, 
	find_prefix,
	add_word_to_trie,  
	look_for_words, 
	look_for_words_beginning_with,
	find_matching_child_node
	)

import pytest
from grappa import should

'''FIXTURES '''

SAMPLE_LIST = ["한","한국","왜","이름"]

@pytest.fixture
def prepopulated_trie():

	root = create_root_node()

	for word in SAMPLE_LIST:
		add_word_to_trie(root, word)

	return root

'''
TESTS

'''

def test_look_for_words_beginning_with(prepopulated_trie):

	root = prepopulated_trie

	# Case where prefix displays all results
	results_1 = look_for_words_beginning_with(root, "한")
	sorted(results_1) | should.be.equal.to(["한", "한국"])

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

	results | should.be.equal.to(SAMPLE_LIST)


def test_add_word_to_trie():
	root = create_root_node()

	add_word_to_trie(root, "한국")

	child_1 = get_single_child(root)
	child_1.letter | should.be.equal.to("한")

	child_2 = get_single_child(child_1)
	child_2.letter | should.be.equal.to("국")

'''TEST HELPER FUNCTIONS '''
def get_single_child(parent: Node):
	return parent.children[0]
