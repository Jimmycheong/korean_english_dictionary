'''check_definition.py

'''
import pickle 
import sys

from functions.trie_functions import find_definition

LINE = "---"
LONG_LINE = LINE * 10
INPUT_FILE = "resources/korean_pickle.pkl"

def main(prefix):
    
    with open(INPUT_FILE, 'rb') as file:
        trie = pickle.load(file)

    definition = find_definition(trie, prefix)

    print(f'''\t{prefix}:\n\t{definition}\n''')

if __name__ == '__main__':

    if len(sys.argv) != 2: 
        raise IOError("Please enter a single keyword to search")

    prefix = sys.argv[1]
    print("prefix: {}".format(prefix))
    main(prefix)
