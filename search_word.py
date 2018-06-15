'''search.py

A program built to search for words using a prefix

'''
import pickle 
import sys

from functions.trie_functions import look_for_words_beginning_with

LINE = "---"
LONG_LINE = LINE * 10
INPUT_FILE = "../resources/korean_pickle.pkl"

def main(prefix):
	
    with open(INPUT_FILE, 'rb') as file:
        trie = pickle.load(file)

    suggestions = look_for_words_beginning_with(trie, prefix)

    print(f'''Search term: {prefix}
            {LONG_LINE}
            Complete list of suggestions: 
            {LONG_LINE}'''
    )

    for word in suggestions: 
        print(f'''\t{word}\n\t{LINE}\n''')

if __name__ == '__main__':

    if len(sys.argv) != 2: 
        raise IOError("Please enter a single keyword to search")

    prefix = sys.argv[1]
    print("prefix: {}".format(prefix))
    main(prefix)
