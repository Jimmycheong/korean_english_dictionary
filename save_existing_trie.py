'''save_existing_trie.py

Dump all existing terms and corresponding trie into a JSON file

TODO: Write logic of saving an exist after it has been updated, containing new terms and definitions.

'''
import pickle 
import sys

from functions.trie_functions import look_for_words

LINE = "---"
LONG_LINE = LINE * 10
INPUT_FILE = "resources/pickles/korean_pickle.pkl"

def main():
    
    with open(INPUT_FILE, 'rb') as file:
        trie = pickle.load(file)

    all_words = look_for_words(trie)

    json_dict = {}

    for word in suggestions: 
        print(f'''\t{word}\n\t{LINE}\n''')

if __name__ == '__main__':
    main()